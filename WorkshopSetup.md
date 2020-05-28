Hands On Lab

SETUP

# Create the Required Resources in your preferred region.

* Data Factory. 
* Databricks cluster. 
* Storage account. Setup as a data lake gen 2 storage.
* Synapse DW. Scale down to 100 DWU. 

![](media14/media/image1.png)

# Setup the Databricks cluster
* We used the default setup but set autoscaling to upto 8 nodes and 300 mins for the allowed idle time before terminating. 
* Mount the Lake as local storage using the provided notebook
* Get an access token for your user. You’ll need this when configuring the final pipeline.

# Follow the workshop instructions

* Create the first three Data Factory Artifacts, validate and run them. Move them to a pipeline folder called "Reference".
* Run the notebook provided to wrangle the data.  
* Create the fourth pipeline that copies the data to Synapse
* Build the Dashboard connecting to Synapse
* Build the final pipeline making changes (watch the video) as required.
* Update the dashboard

# Create Guest Users
* Activate an org wide azure subscription from within the office subscription. 
* We used the format guestuserX@yourdomain.com and set a common password for everyone. 
* these users need to have an E3 license and are linked to the azure subscription you setup within this domain.
* From within the Azure resource group invite each guestuser. Then access the guestuser email, accept the invite, login to azure, set the default directory as microsoft and that should make the resource group now visible to the user. 

# Virtual Workshop Best practices

* The audience does the simpler, non-parameterized, covid-19 data copy pipeline only. If any user is moving faster, then they can do the other two pipelines and the extended paramaterized version too. You can also demonstrate how parameters work as well. 
* we recommend at least 1 helper per 4-6 people doing the hands on. 
* We recommend having 3 speakers
* Speaker 1 is the main session facilitator who does the introduction, and next steps along with re-iterations of specific concepts.
* Speaker 2 is the person who runs the actual hands on.
* For virtual sessions, pick one user, preferably the one with the least experience in Azure and get them to share their screen and walk them through the workshop while the rest follow on their own systems. This sets the speed for the workshop.
* For 10 minutes of hands on (at a CSA's speed),you need about 2 hours in total of workshop time everything included.
* Some basic slides are provided for your reference, but limit teaching time to a max of 30 minutes for every 2 hour segment.
* Speaker 3 acts as a second speaker for the teaching sets. This also give the other speakers time to prep for the next piece.
* Most organizations seem to be locked down and cant access our teams or azure easily. This is why we create ready-to-go and reusable guestusers. You still need to test access with a friendly using these guest users. In some cases the users may need to use his mobile hotspot to get past all walls.  
* Power BI Desktop wont install on a Mac and some users may need to alerted to that. You will need a windows machine to play. 
* Mixing it up with additional demos (Cognitive Services, Auto ML, Knowledge Mining etc)in the last session sets the stage for what they could do together with their data and this amazing template.
