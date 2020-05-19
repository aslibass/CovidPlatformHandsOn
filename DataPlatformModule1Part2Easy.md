Hands On Lab

MODULE I: DATA INGESTION

COVID-19 Dataset

**MODULE 1:**

Data Ingestion with Azure Data Factory

# Objective 2 – Create a Pipeline to Copy Daily COVID-19 Data with Parameters to the Data Lake 

**Pre-requisites:**

  - Azure subscription with Azure Data Factory Instance

  - Completed Objective 1 of Module 1: Creating a pipeline to copy
    country code dataset to the Azure Data Lake

**Learning Outcomes for Module 1:**

  - Importing COVID-19 Data from Github

  - Creating a linked service to link your Azure Storage account to the
    data factory. The linked service has the connection information that
    the Data Factory service uses at runtime to connect to it

  - Creating and validating a pipeline with specified parameters to copy
    the COVID-19 data to Azure Data Lake

<!-- end list -->

1.  Create a new pipeline through selecting the **plus (+)** button and
    click on **Pipeline**

![A screenshot of a cell phone Description automatically
generated](media12/media/image1.png)

2.  In the **general** tab, specify the **pipeline name** i.e. Covid
    Latest Pipe. You will see the name of your pipeline appear on the
    left hand panel under Factory Resources.

![](media12/media/image2.png)

3.  Next, click on the **move and transform** section and drag the
    **‘copy data’** function and rename it to be ‘CovidDataCopy’ in
    the **General** panel.

![](media12/media/image3.png)

4.  The dataset we will be working with for this module can be found
    here:
    <https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports>

![](media12/media/image4.png)

![](media12/media/image5.png)

5.  Next up, we are going to **create a new source**. Click on the
    **source tab** and select the **(+)** button to **add a new
    dataset.**

![](media12/media/image6.png)

6.  On the New Dataset panel on the right hand side, select ‘**HTTP’**
    and click continue.

![](media12/media/image7.png)

7.  Given our raw data from Github is in a csv file click the
    **DelimitedText** option and click **Continue**.

![](media12/media/image8.png)

8.  In the **Set Properties** panel rename the file to
    ‘CovidDataSource’.

![](media12/media/image9.png)

9.  Under the **Linked Service** heading click ‘**new’**.

10. **Name** the linked service to ‘HTTPServerReferenceLinkedService’

11. **Copy** the base URL of the raw Github csv file as shown below
    <https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/>

12. **Set authentication** to Anonymous

![](media12/media/image10.png)

13. Click **Test connection** to verify that the connection is
    successful.

![](media12/media/image11.png)

14. Click **Create**.

15. Input the date of the particular raw csv field in the Relative URL
    field e.g. 05-16-2020.csv![](media12/media/image12.png)

16. Click **OK**.

17. Next, click on **Preview data** as shown

![](media12/media/image13.png)

![](media12/media/image14.png)

18. Next up, we have to define the data lake that we want to copy this
    data to. Navigate to the **Sink** tab and click **new**.

19. Select **Azure Data Lake Storage Gen 2**

![](media12/media/image15.png)

20. Select **Delimited Text**

![](media12/media/image16.png)

21. Input ‘CovidLatest’ in the name field

![](media12/media/image17.png)

22. Select **new linked service**

23. Input fields as shown below:

**Name**: ADLSLSReference

**Azure subscription**: MTC Sydney Azure

**Storage account name**: stcovidhackoutputprod

![](media12/media/image18.png)

24. Click **test connection.**

![](media12/media/image19.png)

25. Next, to set a **file path** click **Browse**

![](media12/media/image20.png)

26. Click on **data** and then select **inputs**

![](media12/media/image21.png)

27. Click **OK**.

28. Click **Validate All**

29. If all the validations are correct, click **Publish All**

30. Next, click **Add trigger**

![](media12/media/image22.png)

31. Click **Trigger now** to trigger the pipeline straight away. When
    prompted for a parameter, input a date value in the format of
    MM-DD-YYYY. Click OK. The pipeline will then start to run.

32. To check how the pipeline is running, go to the **monitor step** in
    Azure Data Factory.

![](media12/media/image23.png)
