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

<!-- end list -->

1.  Create a new pipeline through selecting the **plus (+)** button and
    click on pipeline

![A screenshot of a cell phone Description automatically
generated](media2/media/image1.png)

2.  In the **general** tab, specify the **pipeline name** i.e. Covid
    Latest Pipe. You will see the name of your pipeline appear on the
    left hand panel under Factory Resources.

![](media2/media/image2.png)

3.  Next, click on the **move and transform** section and drag the
    **‘copy data’** function and rename it to be ‘CovidDataCopy’ in
    the **General** panel.

![](media2/media/image3.png)

4.  The dataset we will be working with for this module can be found
    here:
    <https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports>

![](media2/media/image4.png)

![](media2/media/image5.png)

5.  Next up, we are going to **create a new source**. Click on the
    **source tab** and select the **(+)** button to **add a new
    dataset.**

![](media2/media/image6.png)

6.  On the New Dataset panel on the right hand side, select ‘**HTTP’**
    and click continue.

![](media2/media/image7.png)

7.  Given our raw data from Github is in a csv file click the
    **DelimitedText** option and click Continue.

![](media2/media/image8.png)

8.  In the **Set Properties** panel rename the file to
    ‘CovidDataSource’.

![](media2/media/image9.png)

9.  Under the **Linked Service** heading click ‘**new’**.

10. **Name** the linked service to ‘HTTPServerReferenceLinkedService’

11. **Copy** the base URL of the raw Github csv file as shown below
    (<https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/>)

12. **Set authentication** to Anonymous

![](media2/media/image10.png)

13. Click **Test connection** to verify that the connection is
    successful.

![](media2/media/image11.png)

14. Click **Create**.

15. Click OK.

16. Click **Open Source dataset**

![](media2/media/image12.png)

17. To ensure we pull the data with the latest date we must set a
    parameter. Navigate to the Parameters tab and click new.

18. Input ‘FileDate’ in the **name field.**

![](media2/media/image13.png)

19. Navigate to the **Connection** tab. Under the **Relative URL** field
    click on **add dynamic content**, as we want to ensure we always
    pull the latest COVID-19 data.

![](media2/media/image14.png)

20. What we want to do here is get the FileDate as a csv. Input the
    following in the **add dynamic content field:**
    ![](media2/media/image15.png)

21. Click **Finish**

22. Return back to your actual pipeline to test that our parameters
    work. Input a file date to test, and click on **Preview data.**

![](media2/media/image16.png)

23. Next up, we have to define the data lake that we want to copy this
    data to. Navigate to the **Sink** tab and click **new**.

24. Select **Azure Data Lake Storage Gen 2**

![](media2/media/image17.png)

25. Select **Delimited Text**

![](media2/media/image18.png)

26. Input ‘CovidLatest’ in the name field

![](media2/media/image19.png)

27. Select new linked service

28. Input fields as shown below:

**Name**: ADLSLSReference

**Azure subscription**: MTC Sydney Azure

**Storage account name**: stcovidhackoutputprod

![](media2/media/image20.png)

29. Click **test connection.**

![](media2/media/image21.png)

30. Next, to set a **file path** click **browse**

![](media2/media/image22.png)

31. Click on **data** and then select **inputs**

![](media2/media/image23.png)

32. Click **OK**.

33. Click **Validate All**

34. If all the validations are correct, click **Publish All**

35. Next, click **add trigger**

![](media2/media/image24.png)

36. Click **Trigger now** to trigger the pipeline straight away.

37. To check how the pipeline is running, go to the **monitor step** in
    Azure Data Factory.
