![DataPlatformHandsOn](/media/2020-04-14%2017_18_05-MTC%20Sydney%20Data%20and%20AI%20Virtual%20Offerings%20Header.pptx%20-%20PowerPoint.png)
# CovidPlatformHandsOn
Welcome to the github repo for the MTC Sydney Virtual Hands On Workshop where you use Azure Data Factory, Azure Data Lake Storage, Databricks, Synapse and Power BI together to analyse the latest COVID-19 data while also building the automated data pipelines required for the analysis. The workshop has 5 modules. 

This series of exercises seeks to answer the question *does the number of doctors in a country affect the number of COVID-19 cases?* To do this we join the latest covid-19 stats, with statistics from the GHO. You can [view a whiteboard video on the overall approach here](https://1drv.ms/v/s!AvknNlaPoEMyj1TfpPZqIk7Jpaf1?e=FwoUcf). The five modules of this workshop are outlined below. 


## Module 1: Ingesting external data into a data lake with Azure Data Factory Data Pipelines.

**Part 1: Copying country codes data to the lake.**

<!-- * You can use this [Module 1 Part 1 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart1.md)
*  Additionally, you can also download this [video tutorial for part 1](https://1drv.ms/u/s!AvknNlaPoEMyj1al-3retQaZKz3K?e=U0uwIo) 
-->
* You can use this [Module 1 Part 1 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModule1Part1.md)
* Download this [video tutorial for part 1](https://1drv.ms/u/s!AvknNlaPoEMyj1al-3retQaZKz3K?e=U0uwIo) 
* The source file for the data can be found [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)

**Part 2: Copying the latest COVID-19 data from the John Hopkins github repo to the lake.**

<!--* You can use this [Module 1 Part 2 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart2.md)
* Additionally, you can also download this [video tutorial for part 2](https://1drv.ms/v/s!AvknNlaPoEMyj1E_bDj7oXuHWNGP?e=EaIMP9)
-->
* You can use this [Module 1 Part 2 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModule1Part2Easy.md)
* You can use this [Module 1 Part 2 (Extension) Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModule1Part2.md)
* Download this [video tutorial for Part 2 (Extention)](https://1drv.ms/v/s!AvknNlaPoEMyj1E_bDj7oXuHWNGP?e=EaIMP9)
* The source file for the data can be found [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)

**Part 3: Copy GHO data to the lake.**

<!-- * You can use this [Module 1 Part 3 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart3.md)
* Additionally, you can also download this [video tutorial for part 3](https://1drv.ms/v/s!AvknNlaPoEMyj1BmBjpfFvCnFME_?e=F1ap7a)
-->
* You can use this [Module 1 Part 3 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformModulePart3.md)    
* Download this [video tutorial for part 3](https://1drv.ms/v/s!AvknNlaPoEMyj1BmBjpfFvCnFME_?e=F1ap7a)
* The service URL for the API is [https://ghoapi.azureedge.net/api](https://ghoapi.azureedge.net/api). You will need this when you create your OData connection.

## Module 2: Wrangling the data with an open source distributed computing framework, in this case, Databricks.

Here we use in-memory techniques to wrangle the data and save a final set of files to the data lake ready to copy to the warehouse in the next module. 

* For this module you'll need to import [this notebook](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/notebooks/Covid19HackPipeDbNbMain.ipynb) into your databricks workspace and run/modify each cell based on your work in Module 1. 

## Module 3: Copying the final wrangled dataset from the data lake to a Data Warehouse, here, we use Azure Synapse Analytics DW. 

In this module, you create a data pipeline that copys the final dataset from Module 2 into the Azure Synapse Data Warehouse.

* You can download this [video tutorial for Module 3](https://1drv.ms/v/s!AvknNlaPoEMyj1L8nyzEdag_ggu_?e=mfZDfh) for your guidance.

## Module 4: Creating visualizations on the warehouse data using Power BI

![PowerBIDashboardSample](/media/2020-04-23%2013_55_15-CovidHandsOnWorkshop%20-%20Power%20BI%20and%204%20more%20pages%20-%20Work%20-%20Microsoft%E2%80%8B%20Edge.png)

Finally, we create a dashboard that visualizes the data in the data warehouse.

* You can use this [Module 4 Hands On Guide](https://github.com/aslibass/CovidPlatformHandsOn/blob/master/DataPlatformsModule3.md) to do so.
* Additionally, you can also download this [video tutorial for Module 4](https://1drv.ms/v/s!At9MwgSee_b7akmQFrsG2glqEpA?e=cLZzKi)

## Module 5: Creating a full data pipeline that automates all the work done above.

* You can download this [video tutorial for Module 5](https://1drv.ms/u/s!AvknNlaPoEMyj1U9-_2FoDysTLTj?e=7MsuQG) to help guide you.

---
author: Prerita Mehta, Viren Joseph, Microsoft Technology Center, Sydney.
---
