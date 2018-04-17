# NASA NextGen NAS ULI



## Getting Started

Information fusion for real-time national air transportation system prognostics under uncertainty. PARA-ATM is a project undertaken at Arizona State University as part of NASA ULI. It aims to provide a simulation environment to play with cross-domain aviation data for analysis and testing. Being open source, PARA-ATM is meant for learning and research with no commercial aspects to it. It has been developed under the general guidance of Dr. Yongming Liu from the SEMTE department at ASU.

## Installation
```
As of now, the software can be run on Windows and Unix platforms with minor difference between the two. 
The steps are as follows:

1.	Windows:
   a.	Install Python 3.5 from Anaconda here.
   b.	Run the “dependencies.bat”, which will install all necessary Python packages.
   c.	Download and install the latest version of Postgres database from here.
   d.	Create database “paraatm”, with user “paraatm_user” and password  ”paraatm_user”.
   e.	Download and install the latest version of PgAdmin from here.
   f.	Import the database backup “PARA_ATM” into database “paraatm”.
   g.	Import project Information_Fusion into any IDE (Eclipse, IntelliJ, etc.).
   h.	Run “LaunchApp.py” under package PARA_ATM.

2.	Unix:
   a.	Install Python 3.5 from Anaconda here.
   b.	Run the “dependencies.sh”, which will install all necessary Python packages.
   c.	Download and install the latest version of Postgres database from here.
   d.	Create database “paraatm”, with user “paraatm_user” and password ”paraatm_user”.
   e.	Download and install the latest version of PgAdmin from here.
   f.	Import the database backup “PARA_ATM” into database “paraatm”.
   g.	Import project Information_Fusion into any IDE (Eclipse, IntelliJ, etc.).
   h.	Run “LaunchApp.py” under package PARA_ATM.
```
## Application

On running Application.py, the following window would pop up:
 

If you as a user have authentication to use FAA SWIM data, click on the button and the software would tune itself for the same. If not, dismiss this window and proceed with default FlightRadar24 data.

Action Bar:
 

The Action Bar provides an interface to the features and operations that can be performed as part of PARA-ATM. Their functionality are as follows:
Flight: This is a drop-down list wherein all the flight from the database are listed. The flight whose trajectories need to be visualized can be selected.
From and To Date Selectors: The range of date over which the flight’s data needs to be projected can be put in here as DD/MM/YYYY.
Plot Trajectory: Hit this to view trajectory data visualized on the screen as follows:

Execute Command: The command can be put in the space provided above this button. After entering the command, hit this button to view results. Here are few of the inbuilt commands.
-	Airport(PHX): Here, the command Airport() takes the IATA Airport code as the parameter, and plots the airport ground view as follows:
-	PlotGraph(AAL429): This command plots the altitude vs. speed graph for the flight callsign provided as the parameters. 
-	RegressionCurve(AAL429): This command plots the altitude vs. speed regression curve for the flight callsign provided as the parameter.
-	NATS_TrajectorySample(): This command demonstrates integration with NATS, and displays output received.

Like these, users can program custom commands, which has the following template:

![PARA-ATM Commands](https://image.ibb.co/dsJRP7/commandexample.png)

Apply Filters: Aiming to have an all-inclusive platform for data projection and analysis, there are multiple filters that can be toggled based on requirement.
-	Weather Filter: This filter when activated, adds the weather overlay over the map.
-	Airports Filter: The Airports filter marks airports across the US with details about the same.
-	Waypoints: The waypoints filter marks waypoints between the source and destination along the plotted trajectory.
-	Sectors: This filter charts out the different flying sectors that are part of the US airspace.

Run Query: 
This feature allows PARA-ATM to provide an interface to ask questions in natural language about a flight, NTSB Crash data, or related data to get output out of a semantic network, or an ontology. The query can be put into the space given space and hit “Run Query” to execute it. Here’s an example of how it works, though there is a lot more work yet to be done from the query parsing standpoint.

Live Flights:
While working with flight data, it’s always great to have a visualization of how the airspace looks that very instance. PARA-ATM has this feature embedded into it, wherein flight data is pulled in from OpenSky API. Flights are plotted like how they are with FlightRadar24, with flight details popping up by clicking on the aircraft markers.

Documentation and Help:
Hit this button to open the codebase on GitHub, which also includes this documentation. PARA-ATM is an open-source research project, and we are committed to improving it which would provide maximum learning utility. It is highly encouraged that users report bugs and raise issues on GitHub so that it can be fixed at the earliest. To get in touch with questions or suggestions, please reach out to the team.

## Contributors
```
The project has been developed under the guidance of ULI PI Dr. Yongming Liu, with student contributors 
as follows:

Hari Iyer,
Lead Software Engineer,
hari.iyer@asu.edu.

Yutian Pang,
Research Associate,
yutian.pang@asu.edu.
```
