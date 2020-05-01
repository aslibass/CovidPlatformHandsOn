# CovidPlatformHandsOn
Welcome to the github repo for the MTC Sydney Virtual Hands On Workshop where you use Azure Data Factory, Azure Data Lake Storage, Databricks, Synapse and Power BI together to analyse the latest COVID-19 data while also building the automated data pipelines required for the analysis. The workshop has 5 modules. 

This series of exercises seeks to answer the question "does the number of doctors in a country affect the number of COVID-19 cases? To do this we join the latest covid-19 stats, with statistics from the GHO. The process is outlined below. 


## Module 1: Ingesting external data into a data lake with Azure Data Factory Data Pipelines.

**Part 1: Copying country codes data to the lake 

* You can use this [Module 1 Part 1 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart1.md)

**Part 2: Copying the latest COVID-19 data from the John Hopkins github repo to the lake.

* You can use this [Module 1 Part 2 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart2.md)
* Additionally, you can also download this [video tutorial for part 2](https://1drv.ms/v/s!AvknNlaPoEMyj1E_bDj7oXuHWNGP?e=EaIMP9)

**Part 3: Copy GHO data to the lake.

* You can use this [Module 1 Part 3 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart3.md)
* Additionally, you can also download this [video tutorial for part 3](https://1drv.ms/v/s!AvknNlaPoEMyj1BmBjpfFvCnFME_?e=F1ap7a)


## Module 2: Wrangling the data with an open source distributed computing framework, in this case, Databricks.

Here we use in-memory techniques to wrangle the data and save a final set of files to the data lake ready to copy to the warehouse in the next module. 

* For this module you'll need to import [this notebook](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/notebooks/Covid19HackPipeDbNbMain.ipynb) into your databricks workspace and run/modify each cell based on your work in Module 1. 

## Module 3: Copying the final wrangled dataset from the data lake to a Data Warehouse, here, we use Azure Synapse Analytics DW. 

In this module, you create a data pipeline that copys the final dataset from Module 2 into the Azure Synapse Data Warehouse.

* You can download this [video tutorial for Module 3](https://1drv.ms/v/s!AvknNlaPoEMyj1L8nyzEdag_ggu_?e=mfZDfh) for your guidance.

## Module 4: Creating visualizations on the warehouse data using Power BI

Finally, we create a dashboard that visualizes the data in the data warehouse.

* You can use this [Module 4 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModule4.md) to do so.
* Additionally, you can also use this [video tutorial for Module 4](https://1drv.ms/v/s!AvknNlaPoEMyj1M_WQP8HMGGHq-M?e=hph3cH)

## Module 5: Creating a full data pipeline that automates all the work done above.

* A video and hands on guide will be posted here shortly. 

