---
title: Hands On Lab MODULE I: DATA INGESTION
---
Hands On Lab



**MODULE 1:**

Data Ingestion with Azure Data Factory

![](./media/image1.png)

**Pre-requisites:**

  - Azure subscription with Azure Data Factory Instance

**Create a Data Factory**

1.  Select **Create a resource** on the left menu, select **Analytics**,
    and then select **Data Factory**.

![](./media/image2.png)

2.  In the **New data factory** pane, enter a unique name.

> The name of the Azure data factory must be *globally unique*. If you
> see the following error, change the name of the data factory. (For
> example, use **\<yourname\>ADFTutorialDataFactory**). For naming rules
> for Data Factory artifacts, see the [Data Factory - naming
> rules](https://docs.microsoft.com/azure/data-factory/naming-rules) article.

3.  For **Subscription,** select your Azure subscription in which you
    want to create the data factory.

4.  For Resource Group, take **one** of the following steps:

<!-- end list -->

  - Select Use existing and select an existing resource group from the
    drop-down list.

  - Select Create new and enter the name of a resource group.

<!-- end list -->

5.  For **Version**, select V2.

6.  For **Location**, select the location for the data factory.

7.  Select **Create**.

![](./media/image3.png)

**Create an Azure Databricks Linked Service**

1.  After the creation is complete, you will arrive at the **Data
    factory page**. Select the **Author & Monitor** tile to start the
    Data Factory UI application on a separate tab.

![A screenshot of a cell phone Description automatically
generated](./media/image4.png)

2.  ![](./media/image5.png)On the **Let's get started** page, switch to
    the **Edit** tab in the left panel.

3.  Select **Connections** at the bottom of the window, and then
    select **+ New**.

> ![](./media/image6.png)

4.  ![](./media/image7.png)In the **New Linked Service** window,
    select **Compute** \> **Azure Databricks**, and then
    select **Continue**.

5.  In the New Linked Service window, fill in the following fields:

![](./media/image8.png)

  - **Name:**

  - Select the appropriate **Databricks workspace** that your notebook
    will run in

  - **Cluste**r: New job cluster

  - **Domain/Region**: (should autopopulate)

  - Complete the following steps to **generate an access token**:
    
      - ![](./media/image9.png)Click on the **profile icon** in the top
        right corner of your Databricks workspace
    
      - Navigate to **user settings**
    
      - Navigate to the **Access tokens tab**

![](./media/image10.png)

  - Click the **generate new token** button

  - **Copy the generated token** into the Access token field in the New
    Linked Service window (as shown above)

<!-- end list -->

  - **Cluster version:** select **4.2** (with Apache Spark 2.3.1, Scala
    2.11)

  - **Cluster node type**: select **Standard\_D3\_v2** under **General
    Purpose (HDD)** category for this tutorial.

  - **Workers**: 3

  - Select **Finish**

Follow the above process to create linked services for Azure Data Lake
Storage, Azure Blob Storage, OData, HTTP and Azure Synapse as per the
screenshot below:

OData Service URL: <https://ghoapi.azureedge.net/api>

GitHubHTTP Base URL:
<https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports/>

LSGitHub Base URL:
<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/>

LSHttpGitHubCountryCodes Base URL:
<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/>

![](./media/image11.png)

Azure Data Lake Storage

![](./media/image12.png)

Azure Blob Storage

![](./media/image13.png)

OData

![](./media/image14.png)

GitHub HTTP

![](./media/image15.png)

Azure Synapse Analytics

![](./media/image16.png)

**Create Datasets**

1.  Select the plus **(+)** button, and then select **Dataset**.

![](./media/image17.png)

2.  On the **New Dataset** page, select **OData** and then select
    **Continue**

OData is selected in this case we are utilising the World Health
Organisation’s GHO OData API
(<https://www.who.int/data/gho/info/gho-odata-api>)

![A screenshot of a cell phone Description automatically
generated](./media/image18.png)

3.  Click **continue**, to be navigated to the screen below

![](./media/image19.png)

4.  Navigate to the **Connection tab** and input the name of the
    **Linked service** created earlier.

5.  Select the appropriate file path to the data as shown below.

![](./media/image20.png)

Repeat the above steps as follows to cater for COVID-19 Data by John
Hopkins Whiting School of Engineering as follows:
(<https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv>)

6.  Select the plus **(+)** button, and then select **Dataset**.

![](./media/image17.png)

7.  On the **New Dataset** page, select **HTTP** and then select
    **Continue**

![](./media/image21.png)

8.  Select DelimitedText as the format type of your data

![](./media/image22.png)

9.  Set a name for this dataset and select GitHubHTTP as the appropriate
    Linked Service. Then click **OK.**

![](./media/image23.png)

This will bring you to the following screen:

![](./media/image24.png)

10. Navigate to the **Connections** tab and input the following
    parameters:

![](./media/image25.png)

11. Repeat the process above with Lab Technicians and Doctors data as
    follows:

![](./media/image26.png)

![](./media/image27.png)

**Create a Pipeline**

1.  Select the + (plus) button, and then select Pipeline.

![A screenshot of a cell phone Description automatically
generated](./media/image28.png)

2.  In the **General** tab, specify **pipeline name**

![](./media/image29.png)

3.  In the **Activities** toolbox, expand **Move & Transform**. Drag the
    **Copy Data** activity from the Activities toolbox to the pipeline
    designer surface.

> ![](./media/image30.png)

4.  Navigate to the Source tab and input the Source dataset as follows.

![](./media/image31.png)

5.  Navigate to the Sink tab and input the Sink dataset as follows.

![](./media/image32.png)

6.  Click **Validate** on the pipeline toolbar above the canvas to
    validate the pipeline settings. Confirm that the pipeline has been
    successfully validated. To close the validation output, select the
    \>\> (right arrow) button.

**Debug the Pipeline**

1.  To debug your pipeline prior to deploying it to Data Factory, click
    Debug to trigger a test run on the pipeline toolbar above the canvas

![](./media/image33.png)

2.  Confirm that you see the status of the pipeline run on the
    **Output** tab of the pipeline settings at the bottom.

![](./media/image34.png)

**Trigger the Pipeline**

1.  Before you trigger a pipeline, all entities (linked services,
    datasets, pipelines) must be published to Azure Data factory. To
    publish, select **Publish all**.

![](./media/image35.png)

2.  To trigger the pipeline manually, select **Add Trigger** on the
    pipeline toolbar, and then select **Trigger Now**. On the **Pipeline
    run** page, select **Finish**.

Monitor the Pipeline

1.  Switch to the **Monitor** tab on the left. Use
    the **Refresh** button to refresh the list.

> ![](./media/image36.png)

2.  Select the **CopyAndMergeGHO link,** and y the status of the copy
    activity run will be displayed on this page.

3.  To view details about the copy operation, select the **Details
    (eyeglasses image)** link. For details about the properties, see
    Copy Activity overview.

![](./media/image37.png)

4.  Confirm that you see a new file in the **Output** folder.

5.  You can switch back to the **Pipeline runs** view from
    the **Activity runs** view by selecting the **All pipeline
    runs** link.
---
author: Prerita Mehta, Viren Joseph
---
