Hands On Lab

MODULE I: DATA INGESTION

**MODULE 1:**

Data Ingestion with Azure Data Factory

# Objective 1 – Create a Pipeline to Copy the Country Codes Data Set to the Data Lake

# 

![](.\\media\\1/media/image1.png)

**Pre-requisites:**

  - Azure subscription with Azure Data Factory Instance

<!-- end list -->

1.  ![](.\\media\\1/media/image2.png)On the **Let's get started** page,
    switch to the **Edit** tab in the left panel.

2.  The first thing we need to do is **create a folder** for all our
    resources and work. Under the **pipeline** section, click the
    **three dots** for more actions and **create new folder.**

> ![](.\\media\\1/media/image3.png)

3.  Next, **create a new pipeline**. Select the **plus (+)** button and
    click on pipeline. This is going to be a data pipeline to copy stuff
    across

![A screenshot of a cell phone Description automatically
generated](.\\media\\1/media/image4.png)

4.  In the **general** tab, specify **pipeline name** i.e.
    DataCopy\<Name\>. You will see the name of your pipeline appear on
    the left hand panel under Factory Resources. Drag and drop your
    pipeline from the left hand panel to the folder we created in the
    first step.

![](.\\media\\1/media/image5.png)

5.  Next, click on the **move and transform** section and drag the
    **‘copy data’** function and rename it to be ‘CopyCountryCodeData’
    in the **General** panel.

![](.\\media\\1/media/image6.png)

6.  One of the datasets we are going to be working with can be found
    here:
    <https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv>

Click the ‘**raw’** button to see this file in csv format.

![](.\\media\\1/media/image7.png)

![](.\\media\\1/media/image8.png)

7.  Next up, we’re going to **create a new source**. Click on the
    **source tab** and select the **(+)** button to **add a new
    dataset.**

![](.\\media\\1/media/image9.png)

8.  On the New Dataset panel on the right hand side, select ‘**HTTP’**
    and click continue.

![](.\\media\\1/media/image10.png)

9.  Given our raw data from Github is in a csv file click the
    **DelimitedText** option and click Continue.

![](.\\media\\1/media/image11.png)

10. In the **Set Properties** panel rename the file to
    ‘CountryCodeData’.

11. Select the ‘**first row as header’** option.

![](.\\media\\1/media/image12.png)

12. Under the **Linked Service** heading click ‘**new’**.

13. **Name** the linked service to ‘HTTP\<Name\>Github

14. **Copy** the **base URL** of the raw Github csv file as shown below

15. Set **Authentication** type to **Anonymous**

![](.\\media\\1/media/image13.png)

16. Click **Test connection** to verify that the connection is
    successful.

17. Click **Create**.

18. On the Set Properties Page enter **Name** as CountryCode

19. Select HTTP\<Name\>Github as **Linked service**

20. Input the **relative URL** of the raw Github csv file as shown below

21. Select **first row as header**

22. Click **OK.**

![](.\\media\\1/media/image14.png)

23. Select Preview Data

![](.\\media\\1/media/image15.png)

24. On the Data storage read settings page select **Finish**.

![](.\\media\\1/media/image16.png)

25. Verify that a preview of your data is displayed as shown below.

![](.\\media\\1/media/image17.png)

26. Select the **Sink** tab and click **(+) New**

![](.\\media\\1/media/image18.png)

27. Select Azure Data Lake Storage Gen2

![](.\\media\\1/media/image19.png)

28. Select Format as Delimited Text

![](.\\media\\1/media/image20.png)

29. Set **Name** as ‘CountryCodeDL\<Name\>

30. Select **first row as header**

31. Click **new Linked Service**

![](.\\media\\1/media/image21.png)

32. Input Azure subscription as shown below

33. Input Storage account name as shown below

![](.\\media\\1/media/image22.png)

34. Click **Continue**

35. On the **Set Properties** page select **Browse** under the File Path
    heading

![](.\\media\\1/media/image23.png)

36. Select **inputs** as shown below.

![](.\\media\\1/media/image24.png)

![](.\\media\\1/media/image25.png)

37. Next click **Validate all**

38. Once validated, click **Publish all**

39. Next, click **add trigger**, and click **trigger now**

40. Verify that the pipeline has successfully run through the storage
    group.

We have successfully created the Covid Country Data Pipeline. This
process will be repeated twice more to create the remaining pipelines to
be ingested: Covid Dataset and GHO Doctor Count.
