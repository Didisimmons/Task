# WEATHER APP 

[Back To Main README File](README.md)

[View The Deployed Site](https://weathertabs.herokuapp.com/)

## TESTING
<br/>

**Table of Contents** 
1. [Validator Testing](#validator-testing)  
   - [HTML](#html)   
   - [CSS](#css)
   - [PYTHON](#python) 

2.  [Further Testing](#further-testing)

3. [Solved Bugs](#solved-bugs)

4. [Future Improvements](#future-improvements)

<br/>

### **VALIDATOR TESTING**
#### **HTML**


### **SOLVED BUGS**

1. Issues arose while retrieving the API data for the weather app and storing it in the form, preventing the user from accessing the API data. This would allow the user to store weather metadata in the database for each sensor that was registered. Due to time constraints, I was unable to store the weather meta data in the registered sensor's database when attempting to meet the challenge's second requirement of receiving new metric values as the weather changes for the sensor via an API call. However, after some research, I discovered a workaround by using the registered sensor's city and country names to call the open weather API and gain access to weather data of the sensor.

This was fixed by creating a for loop and calling the URL in the registered sensor to use its parameters to retrieve meta data for the sensor and attaching the meta data to each sensor registered/created. Including this function allowed the user to register a sensor and access basic sensor meta data on the homepage.

2. In order to view more details for each sensor issues arose initially setting the url for the result page which displays more meta data weather information for a particular sensor. When the variable  was used in the home template where all the sensors where called the id through an error stating the id was not valid. This was fixed by calling the id in the for loop present in the view used to access the API URL for the sensor , once this was added to the for loop , I was able to call the id variable in the home template.

Issues arose initially setting the url for the result page which displays more meta data weather information for a specific sensor in order to view more details for each sensor. When the variable``` sensor_id ``` was used in the home template where all the sensors were called, an error message stating that the id was not valid appeared. This was fixed by including the id variable in the for loop of the view used to access the API URL for the sensor; once this was included in the for loop, I was able to call the id variable in the home template ```sensor_weather.id ``` and set the url in urls.py.


3. If a user decides to delete a sensor, a pop-up modal appears asking the user to confirm their action; if the user clicks the delete button, the user is returned to the homepage. However, if the user clicks the cancel button, they are returned to the home page, which should not happen. When I tried to add the sensor id to be passed through the result function on the cancel button, the error id not valid kept appearing, and due to time constraints, this could not be fixed but is one of the future improvements.


4. When deploying to Heroku, there were complications with pushing the remote repository to Heroku. Heroku continued to display errors related to conflicts in the remote repository, stating that another repo was using the details. The data was pulled in order to merge the remote repository ahead of the local repository, but a conflict arose every time I tried to pull and push the code to heroku. The push was rejected, and the error message was the same. After some investigation, I deleted the heroku app and created a new app using the heroku cli, and I was able to push the code to heroku without any merge conflicts/error messages.

5.  When deploying our static files to Heroku, white noise was installed in order to deploy our static files as a self-contained unit to Heroku. Initially, when we pushed our code to github, we received an error message stating that collectstatic should be disabled, but this was ignored because we had static files such as our stylesheet. Adding the static root file and the static files directory path to the settings.py file was supposed to allow us to load the static files on our deployed site, but this did not work. So the command "' heroku config:set DISABLE COLLECTSTATIC=1 "' was executed as advised, then whitenoise was installed, and finally the collectstatic command was executed, and the site was able to deploy with static files.

6. In order to get weather metrics such as temperature, humidity and wind speed etc, the openweather API was used to fetch data of the registered sensor. There were some limitations when using the open weather API such as to retrieve hourly data for the past 7 days or a month the user would need to subscribe to the API pro account which involves card payment.Another option was to use the longitude and latitude of the city but because we were not storing those data in the database we were unable to implement the forecast for 4 days that was provided in one of their weather API documentation. This would have involved us using the Geocoding API. 

### **Future Improvements**
To keep the challenge within the timeframe, some functionalities that could be implemented to improve the site have been left out. 

* Provide a more detailed testing report that includes manual site testing.

* Include a button on the single view page that allows the user to view the average temperature of the day based on the time stamps provided on the page.

* Allow the user to save weather metadata in their database and update the values with real-time weather metadata from the API if they are logged in as the user and can perform CRUD functions.

* Add restrictions in the Sensor Form not to allow duplicate forms of the same city and country name in the database and to esure that the city and country provided are actual places and not just formed locations. 