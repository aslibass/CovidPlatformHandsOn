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

#dbutils.fs.mount(
#source = "wasbs://<your-container-name>@<your-storage-account-name>.blob.core.windows.net",
#mount_point = "/mnt/<mount-name>",
#extra_configs = {"fs.azure.account.key.<your-storage-account-name>.blob.core.windows.net":"<access-key>"})

dbutils.fs.mount(
source = "wasbs://outputs@stcovidhackoutput.blob.core.windows.net",
mount_point = "/mnt/coviddata",
extra_configs = {"fs.azure.account.key.stcovidhackoutput.blob.core.windows.net":"exnopN56JLbbkuZxx5VLX6sJqH7pop7fWaXEgYgMkt5OY2EtqqppFako7t3wOca7oYUbThKVwmMX4wpv4bwafA=="})

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Check for the lastest file names

# COMMAND ----------

display(dbutils.fs.ls("/mnt/coviddata/"))
        

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #Wrangle the Doctor Data

# COMMAND ----------

filepath2="/mnt/coviddata/DoctorsGlobal"
#filepath3=""/mnt/coviddata/LabTechsGlobal""

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

doctorlatest.write.csv('/mnt/coviddata/DoctorCountLatestYear.csv')

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC #Wrangle the COVID Data

# COMMAND ----------

filepath = "/mnt/coviddata/03-29-2020.csv"

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### infer the schema and load the data into a spark dataframe

# COMMAND ----------

covidraw = spark.read.format('csv').options(header='true', inferSchema='true').load(filepath) 


# COMMAND ----------

display(covidraw)

# COMMAND ----------

