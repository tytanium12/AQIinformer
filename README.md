# AQIinformer
1) Abstract
The AQI informer ("AQIinformer") gives you an up-to-date picture of the Air Quality Index (AQI) in your area. The at-a-glance interface gives you key information about what the air quality is like in surrounding areas, what it was like up to 3 days in the past, the current AQI, and what it will be like up to 3 days in the future. The app also gives key information about the weather in your area.

2) For Hiring Managers, Recruiters, and Other Employers
As a part of my portfolio, these are some of the main skills I demonstrated when writing the code to construct this app:

-Proficiency in the python coding language
-Mastery of several python libraries including datetime, tkinter, matplotlib, requests, pandas, math, geopy, pytz, timezonefinder, and geocoder
-Object Oriented Programming (OOP). I divided the code into 4 separate modules to oversee the different parts of the user interface. I created classes and wrote relevant functions for those classes, streamlining the final configuration of the user interface and making it easy to update the code in the future.
-Use of resources including library documentation, stackoverflow, google, and AI (chatGPT) to write the code and construct the app
-Fetching information from an API and using processing that information into usable graphs and summaries
-Working with databases coming in as JSON files
-Design and creation of an interactive user interface using the tkinter library
-Creation of an informational graphic using matplotlib to draw and display the information in a unique way
-Version control using GitHub
-Software development lifecycle
-Problem solving
-Working with datetime objects
-Using coordinates and normalizing time from different time zones and types (local, GMT, etc)
-Ability to write thorough and concise documentation

3) Introduction
This app was inspired by reading an article listing potential portfolio projects for python programmers. The prompt was to construct a weather app. As much as I love the weather, I felt like just displaying the current temperature and wind speed wasn't enough (although this app does that too!). I decided to focus on the Air Quality aspect of weather and weather forecasting. Part of this is admittedly selfish. I, as an asthmatic, have a harder time breathing on days with poor air quality. Because of this I know that there are many other people with sensitivities to poor air quality.

So, for all of my fellow "hard-of-breath-ers", this app is for you. And for anyone else who might be interested in an at-a-glance look at the air quality in their area, and in the future.

3.1) What is the Air Quality Index (AQI) and Why is it Useful?
The Air Quality Index (AQI) is a numerical scale used to communicate how polluted the air currently is or how polluted it is forecast to become. It is an important tool for understanding the potential health impacts of air pollution on a population. The AQI is used by governments and organizations to report daily air quality, with different levels corresponding to different levels of health concern.

The AQI encompasses several pollutants including ground-level ozone (O₃), particulate matter (PM10 and PM2.5): fine particles that can penetrate deep into the lungs, carbon monoxide (CO), sulfur dioxide (SO₂), nitrogen dioxide (NO₂).

AQI Scale: The AQI typically ranges from 0 to 500. The higher the AQI value, the greater the level of air pollution and the greater the health risk. The AQI is divided into several categories that describe the level of concern:

0 to 50: Good — Air quality is considered satisfactory, and air pollution poses little or no risk.
51 to 100: Moderate — Air quality is acceptable; however, there may be a concern for some people, especially those who are unusually sensitive to air pollution.
101 to 150: Unhealthy for Sensitive Groups — Members of sensitive groups, such as children, the elderly, and people with respiratory conditions, may experience health effects.
151 to 200: Unhealthy — Everyone may begin to experience health effects, and members of sensitive groups may experience more serious effects.
201 to 300: Very Unhealthy — Health alert: everyone may experience more serious health effects.
301 to 500: Hazardous — Health warnings of emergency conditions; the entire population is more likely to be affected.

Health Impact: The AQI helps individuals understand how polluted the air is and what precautions they might need to take. For example:
a) On days with high AQI values, people with asthma or heart disease might need to limit outdoor activities.
b) At extreme levels, like Hazardous (AQI over 300), it is recommended for everyone to avoid outdoor exposure, as the pollution levels can be dangerous.

Reporting and Use: Governments and environmental agencies monitor air quality and issue daily AQI reports to inform the public. These reports may be provided via news outlets, mobile apps, or websites. In many countries, it is part of an alert system that notifies citizens of unsafe conditions.

As another example:
If an AQI report shows a value of 160, it falls under the "Unhealthy" category. People with respiratory issues or children might be advised to stay indoors, and the general population might be warned about potential health risks from outdoor activities.

In short, the AQI is a standardized way to measure and communicate the risks of air pollution to the public, allowing people to take appropriate precautions for their health based on current conditions.

3.2) About the AQIinformer App
The AQIinformer app allows you to input any location using latitude and longitude coordinates (or automatically fetch your coordinates based on your IP address) and display relevant weather and air quality information in a simple user interface. The information includes city, current local time and date, current AQI, current temperature, precipitation in the past hour, and current wind speed.

The AQIinformer app also displays two unique graphs to give you at-a-glance insight into the air quality around you. One chart displays information about what the AQI was in the past, what it is now, and what it will be in the future. The other chart shows what the AQI is in the location you selected, along with the AQI 20 miles in each cardinal direction. This gives you an quick look at the overall air quality in your area. Both charts are color-coded with the Air Quality Index "Levels of Concern" published by the EPA at airnow.gov/aqi/aqi-basics. More information on the charts will be given later in the readme.

4) Downloading and Running
To check out the app for yourself, just follow these steps:

a) Download all four files:
userInterface.py
fetchCurrent.py
areaGraph.py
timeGraph.py

b) Put all four files in the same directory in your IDE of choice (I use PyCharm).

c) Open userInterface.py and run it

d) AQIinformer is now operating on your device!

Note: This app was made and tested on Windows 11

5) How to Use the AQIinformer App
To use AQI informer, all you have to do is provide a set of coordinates. AQIinformer will do all of the rest! You can use any map or method of your choice to obtain coordinates of interest. I recommend getting coordinates from Google Maps. Simply search or navigate to a city or area of interest, right click on the map, and the coordinates will be displayed.

For inputting coordinates, I recommend using 2 decimal places. E.g. Latitude: 47.65 and Longitude: -122.31.

Those just happen to be the default coordinates which will lead you to Bagley Hall on the University of Washington Campus in Seattle. Bagley Hall is the original chemistry building.

The inputs for the latitude and longitude coordinates are in the upper left of the window.

You can also obtain your own current coordinates (estimated based on your IP address) by simply clicking the "Get Current Location" button directly below the latitude and longitude inputs. This will populate the latitude and longitude boxes with your current coordinates automatically.

All that's left now is to press the "Refresh Data" button that is also directly below the latitude and longitude input boxes, and to the left of the "Get Current Location" button. Once you press "Refresh Data" the program will run to obtain the latest AQI and weather information at the selected coordinates. The information summary and graphs will also update according to the new information.

Directly below the "Refresh Data" and "Get Current Location" buttons lies an information summary. All of the information is relevant to the coordinates you input at the time you hit the "Refresh Data" button. A description of the information provided follows:

Current City: Displays the nearest current city to the input coordinates, if one can be found
Current Time: Displays the local time at the coordinates you input
AQI (Current): Displays the most recent AQI reading at your selected location
Temperature: Displays the most recent temperature reading at your selected location in degrees Fahrenheit
Precipitation (past 1 hour): Displays how much precipitation has fallen in the selected location in the past 1 hour. Displayed in inches
Wind Speed: Displays the current wind speed at 2 meters above the surface for the selected location

5.1) AREA GRAPH:
To the right of the basic inputs, buttons, and information is an "Area Graph" titled "AQI in Selected Location and Nearby Areas(20 miles in each direction). This graph shows important information about the AQI in your area, and the areas around you.

In the center of the graph is a circle representing the location you selected by inputting your chosen coordinates. The quadrants at the top, sides, and bottom of the graph are labeled North, East, South, and West. These quadrants represent the AQI as measured at a point approximately 20 miles in the direction indicated. So, for example, the quadrant labeled "North" gives the AQI for an area that is approximately 20 miles to your North.

The circle and each quadrant are color coded according the AQI severity chart published by the EPA at airnow.gov/aqi/aqi-basics. So if the current AQI is low at 32, indicating low pollutants, then the circle or quadrant will be displayed with a green background. On the other hand, if the current AQI is high and unhealthy at 174, then the circle or quadrant will have a red background. More details in the next section about the Legend.

This "Area Graph" gives you a quick at-a-glance look at the air quality in your surrounding areas. Perhaps you have a beach to the West and mountains to the East and you want to decide what to do outdoors. You take a look at your AQIinformer app for your current location and discover that the AQI at the beach is high, at 140. Meanwhile, the AQI to the East in the mountains is just 41. You decide to head to the mountains for a nice hike in clear air.

This is just one example of how the area map could be useful.

5.2) LEGEND:
The Legend is just below the basic inputs, buttons, and information as well as just below the "Area Graph". It is directly above the "AQI Over Time" graph. This legend applies to BOTH graphs.

The Legend displays the color codes, descriptors, and AQI ranges for the AQI severity chart published by the EPA at airnow.gov/aqi/aqi-basics. The lower the AQI the less polluted the air is. The higher the AQI the more polluted the air. The Legend helps you determine if the air quality is a hazard for you or safe for you to go out.

You can find out more information about what each color category means at airnow.gov/aqi/aqi-basics.

5.3) TIME GRAPH: 
Directly below the Legend, at the bottom of the app window is the "Time Graph" or "AQI Over Time" graph.

This graph shows you the AQI at your selected location over a time span from 3 days ago (-72 hr) to a forecast of 3 days into the future (72 hr). The current AQI is shown in the middle as "NOW". The times then proceed both to historical data in the past and future forecasts at intervals of 1 hr, 3 hr, 8 hr, 24 hr, 48 hr, and 72 hr.

This feature is useful for many reasons. One reason is that it gives you historical data at a glance. This could be useful if you've noticed that you were having labored breathing for the past few days, but today you suddenly feel better. The "Time Graph" might show that the AQI was high for the past few days, but a breeze came in and cleared the AQI to the "Good" level today, explaining your breathing experiences. 

Another reason is that you might notice a trend of worsening AQI across the graph. The historical data might show a low AQI for the past few days, moderate AQI for today, and worsening AQI in the forecast. This could give you time to prepare for worsening air quality, such as closing windows and re-planning outdoor activities.

As with the "Area Graph", the "Time Graph" is color coded according to the AQI scale shown in the Legend. Each box displays the time period, the AQI, and is filled with the corresponding color from the Legend.

6) Dependencies
Package: Version: Latest Version:
attrs	24.2.0	24.2.0
cattrs	24.1.2	24.1.2
certifi	2024.8.30	2024.8.30
cffi	1.17.1	1.17.1
charset-normalizer	3.4.0	3.4.0
click	8.1.7	8.1.7
colorama	0.4.6	0.4.6
contourpy	1.3.1	1.3.1
cycler	0.12.1	0.12.1
decorator	5.1.1	5.1.1
flatbuffers	24.3.25	24.3.25
fonttools	4.55.0	4.55.2
future	1.0.0	1.0.0
geocoder	1.38.1	1.38.1
geographiclib	2.0	2.0
geopy	2.4.1	2.4.1
h3	4.1.2	4.1.2
idna	3.10	3.10
kiwisolver	1.4.7	1.4.7
matplotlib	3.9.3	3.9.3
numpy	2.1.3	2.1.3
openmeteo_requests	1.3.0	1.3.0
openmeteo_sdk	1.18.0	1.18.0
packaging	24.2	24.2
pandas	2.2.3	2.2.3
pillow	11.0.0	11.0.0
pip	24.3.1	24.3.1
platformdirs	4.3.6	4.3.6
py	1.11.0	1.11.0
pycparser	2.22	2.22
pyparsing	3.2.0	3.2.0
python-dateutil	2.9.0.post0	2.9.0.post0
pytz	2024.2	2024.2
ratelim	0.1.6	0.1.6
requests	2.32.3	2.32.3
requests-cache	1.2.1	1.2.1
retry	0.9.2	0.9.2
retry-requests	2.0.0	2.0.0
six	1.16.0	1.17.0
timezonefinder	6.5.7	6.5.7
tzdata	2024.2	2024.2
url-normalize	1.4.3	1.4.3
urllib3	2.2.3	2.2.3

7) Changelog
12/04/2024 - Initial Version
12/05/2024 - Version 1.0 - Increase font sizes, Rename get_current_time function in fetchCurrent to get_rounded_time, Add function get_local_time to show local time at the selected coordinates, Add .gitignore, Add readme, Change geolocater User Agent to "friends_of_aqiInformer_app" and recommend you change to your own.


