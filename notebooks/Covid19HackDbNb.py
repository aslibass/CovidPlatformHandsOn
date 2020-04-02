# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC #Notebook shortcuts
# MAGIC 
# MAGIC ### shift+enter = Run cell and move to the next one
# MAGIC 
# MAGIC ### ctrl+alt+P = insert cell above
# MAGIC ### ctrl+alt+N = insert cell below
# MAGIC 
# MAGIC ### ctrl+alt+up = move cell up
# MAGIC ### ctrl+alt+down = move cell down
# MAGIC 
# MAGIC 
# MAGIC for more shortcuts go to https://docs.microsoft.com/en-us/azure/databricks/notebooks/notebooks-use

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Connect to our Data Lake

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ###create a mount point using our ADLSV2 as the storage point. 
# MAGIC This way we can easily get to the data everytime the cluster restarts. 

# COMMAND ----------

dbutils.fs.unmount("/mnt/coviddata")

# COMMAND ----------

dbutils.fs.ls("/mnt/")

# COMMAND ----------



# COMMAND ----------

dbutils.fs.mkdirs("/mnt/coviddata/inputs")

# COMMAND ----------

dbutils.fs.mkdirs("/mnt/coviddata/outputs")

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC The below cells only work the first time, when the cluster is setup. 

# COMMAND ----------

#dbutils.fs.mount(
#source = "wasbs://<your-container-name>@<your-storage-account-name>.blob.core.windows.net",
#mount_point = "/mnt/<mount-name>",
#extra_configs = {"fs.azure.account.key.<your-storage-account-name>.blob.core.windows.net":"<access-key>"})



dbutils.fs.mount(
source = "wasbs://outputs@stcovidhackoutput.blob.core.windows.net",
mount_point = "/mnt/coviddata/outputs",
extra_configs = {"fs.azure.account.key.stcovidhackoutput.blob.core.windows.net":"exnopN56JLbbkuZxx5VLX6sJqH7pop7fWaXEgYgMkt5OY2EtqqppFako7t3wOca7oYUbThKVwmMX4wpv4bwafA=="})



# COMMAND ----------

dbutils.fs.mount(
source = "wasbs://inputs@stcovidhackoutput.blob.core.windows.net",
mount_point = "/mnt/coviddata/inputs",
extra_configs = {"fs.azure.account.key.stcovidhackoutput.blob.core.windows.net":"exnopN56JLbbkuZxx5VLX6sJqH7pop7fWaXEgYgMkt5OY2EtqqppFako7t3wOca7oYUbThKVwmMX4wpv4bwafA=="})

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Check file structure is setup

# COMMAND ----------

display(dbutils.fs.ls("/mnt/coviddata/"))
        

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Check all the required files are visible

# COMMAND ----------

display(dbutils.fs.ls("/mnt/coviddata/inputs"))

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #Wrangle the Doctor Data

# COMMAND ----------

filepath2="/mnt/coviddata/inputs/DoctorCountLatest.csv"


# COMMAND ----------

# MAGIC %md 
# MAGIC ###infer the schema and load the data to a spark data frame. 
# MAGIC ### cache the data for faster operations

# COMMAND ----------

doctorraw = spark.read.format('csv').options(header='false', inferSchema='true').load(filepath2)
doctorraw.cache()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### check if schema was inferred correctly

# COMMAND ----------

doctorraw.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Display the data in a nice readable format

# COMMAND ----------

display(doctorraw)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### focus on the columns we want to work with

# COMMAND ----------

display(doctorraw.select("_c3","_c5","_c15"))

# COMMAND ----------

doctorraw.select("_c3","_c5","_c15").show()

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### filter the data so that there is only the doctor per 10k count for the most recent year for each country in the list. We only need the latest year. 

# COMMAND ----------

doctorlatest=doctorraw.groupBy("_c3").max("_c5","_c15")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### just confirm that Australia exists in the data set we're pulling

# COMMAND ----------

doctorlatest.filter("_c3= 'AUS'").show()

# COMMAND ----------

display(doctorlatest)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### rename the columns

# COMMAND ----------

doctorlatest=doctorlatest.withColumnRenamed("_c3",'COUNTRY').withColumnRenamed("max(_c5)",'YEAR').withColumnRenamed("max(_c15)",'DoctorsPer10k')

# COMMAND ----------

doctorlatest.printSchema()

# COMMAND ----------

doctorlatest.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### save it to csv on our data lake

# COMMAND ----------

doctorlatest.write.csv('/mnt/coviddata/outputs/DoctorCountLatestYear')

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ###Load the country code data

# COMMAND ----------

filepath3="/mnt/coviddata/inputs/UID_ISO_FIPS_LookUp_Table.csv"

# COMMAND ----------

countrycodes = spark.read.format('csv').options(header='true', inferSchema='true').load(filepath3)

# COMMAND ----------

countrycodes.printSchema()

# COMMAND ----------

countrycodes.show()

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### just want country region and iso3

# COMMAND ----------

countrycodeiso3=countrycodes.select("iso3","Country_Region").distinct()

# COMMAND ----------

countrycodeiso3.filter("iso3='AUS'").show()

# COMMAND ----------

countrycodeiso3.write.csv('/mnt/coviddata/outputs/CountryCodesISO3')

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC #Wrangle the COVID Data
# MAGIC 
# MAGIC ### load the covid data and summarize by country
# MAGIC ### join the summarized data with the count of doctors and country codes 

# COMMAND ----------

filepath = "/mnt/coviddata/inputs/04-01-2020.csv"

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### infer the schema and load the data into a spark dataframe

# COMMAND ----------

covidraw = spark.read.format('csv').options(header='true', inferSchema='true').load(filepath)


# COMMAND ----------

display(covidraw)

# COMMAND ----------

covidlatest=covidraw.select("Country_Region","Confirmed","Deaths","Recovered").groupby("Country_Region").sum("Confirmed","Deaths","Recovered")

# COMMAND ----------

display(covidlatest)

# COMMAND ----------

covidlatest.write.csv('/mnt/coviddata/outputs/CovidLatest')

# COMMAND ----------

doctorlatest.show()

# COMMAND ----------

countrycodeiso3.show()

# COMMAND ----------

from pyspark.sql.functions import col
doctoriso3=doctorlatest.join(countrycodeiso3,col("COUNTRY")==col("iso3"))

# COMMAND ----------

doctoriso3.select("COUNTRY","YEAR","DoctorsPer10k","Country_Region").filter("COUNTRY = 'AUS'").show()

# COMMAND ----------

coviddoctors = covidlatest.join(doctoriso3, doctoriso3.Country_Region == covidlatest.Country_Region)

# COMMAND ----------

coviddoctors.show()

# COMMAND ----------

coviddoctorselect = coviddoctors.select(covidlatest.Country_Region,"sum(Confirmed)","sum(Deaths)","sum(Recovered)","COUNTRY","YEAR","DoctorsPer10k")

# COMMAND ----------

coviddoctorfinal=coviddoctorselect\
.withColumnRenamed('sum(Confirmed)','Confirmed')\
.withColumnRenamed('sum(Deaths)','Deaths')\
.withColumnRenamed('sum(Recovered)','Recovered')\
.withColumnRenamed('COUNTRY','Iso3')\
.withColumnRenamed('YEAR','YearOfDoctorCount')

# COMMAND ----------

coviddoctorfinal.printSchema()

# COMMAND ----------

coviddoctorfinal.write.csv('/mnt/coviddata/outputs/CovidDoctorCombined')

# COMMAND ----------

