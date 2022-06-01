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

2. [Manual Testing](#manual-testing)   
   - [HOMEPAGE](#homepage)   
   - [RESULT PAGE](#result-page)
      - [DELETE MODAL](#delete-modal) 

3. [Further Testing](#further-testing)

4. [Solved Bugs](#solved-bugs)

5. [Future Improvements](#future-improvements)
<br/>

### **VALIDATOR TESTING**
#### **HTML**
*  [W3C Markup Validation](https://validator.w3.org/): This is also used to validate our newly created webpages. However some errors were found such as  

- On the home page the errors are 
      - misuse of aria-label
      - Img element has no alt attribute
      - 



#### **CSS**
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/): This is used to validate the CSS code that is used on all webpages . The validator passes our code as error-free. 

#### **PYTHON**
* [Pep8 Online validator](http://pep8online.com/): This was used to run our Python code to ensure that all errors were removed, such as trailing whitespace. When this was run through the validator, it was discovered that some whitespaces were present, as well as some variables that had been flagged and resolved, but only errors such as

 -  On the views.py file the url = "http://api.openweathermap.org/data/2.5/weather?q={},{}&units=imperial&appid={}"  line is too long, but breaking it down may affect fetching API data, so erro ignored. 

 - Also on the views.py file "multiple imports on one line" was ignored because it is equivalent to writing in the same line.. 

 With the exception of the errors mentioned above, which were ignored, whitespaces were removed from all codes, resulting in an error-free code.

<br/>

### **MANUAL TESTING**

#### TESTING ALL FEATURES ON EACH PAGE 

#### **HOMEPAGE** 
Some automated testing was performed, but due to time constraints, manual testing was prioritised.

1. . Navigation bar 

    1. Navigate to the Index page (Home) on a desktop by visiting the website. 

    2. Change the screen size of the desktop to that of a tablet device to ensure that the navigation bar is responsive and changes to a hamburger icon as the screen width decreases to that of a tablet or mobile device. Menu items should be hidden in the hamburger icon for medium to small devices.

         When testing responsiveness across different devices, there was no overflow of the navbar. The navbar did not overflow when tested for responsiveness across multiple devices. The navbar functions as expected. 
         
         The navigation bar menu changes to a hamburger icon on a tablet or mobile device, with the menu appearing on the right side of the navbar. 


2. Form   

   1.	Ensure that the user is prompted with a placeholder on the forms and that the form has an autofocus attribute for the country name. 
         
         Carrying out  it is possible to see that placeholders are present on the forms, informing the user of the input required from them, and that the autofocus attribute on country is present. However we changed how the form was beeing rendered which affected its styling. 
         
         This change was made to remove the labels from the forms and replace them with placeholders so that the form fields would be responsive on all screens. On smaller devices, the label was visible to be overflowing, which did not provide the user with a good experience. For smaller and medium-sized devices, the form fields are currently placed above each other, while for larger devices, the fields are placed below each other now.


   2. Confirm that the user must fill out all mandatory fields before submitting the Sensor form. If the fields are not correctly filled out, the user should receive an error message.s

     Testing this on all devices reveals that when a user attempts to register a sensor, they must provide  all fields as they are mandatory fields.   If the fields are not filled out and the user tries to submit a form the user will be notified with a required message . 

     If the user completes  the fields and clicks the "Get weather" button, he or she can view weather metadata of that sensor.

   3. Confirm that when a user clicks the "Get weather" button under the form , the sensor is registered and appears on the home screen. 

     When tested across all devices, it is clear that when the user clicks the "Get weather" button, the sensor is added to the database and the user can view the sensor on the home page. It performs as expected.

<br/>

3. Cards 

   1. Confirm that the sensors are displayed in a card container design on the home page. The card container should include an icon, country, city name, and weather metadata. The card should be responsive, adjusting to each screen size as the screen width decreases.

         With the above-mentioned properties, the sensors are displayed in a card container as expected. As the screen width is reduced, it is clear that the card container is responsive, with the sensor content adapting to the screens as expected. The card has a clean appearance and is visible enough to catch the user's attention.

  2. Confirm that clicking the "View More" button in the product card takes the user to the correct page.

      The button is located on the right side of the card and adjusts to the width of the screen as the width of the screen is changed. When the user clicks the button, he or she is taken to the results page.

<br/>

#### **RESULT PAGE**
   1. Verify that the sensor information for a specific sensor id is displayed on the result page. The page should display the weather temperature for the sensor's six time readings of the day.

      When viewed on all devices, the page renders as expected, displaying the weather temperature for the six time readings of the day. The text responds to screen size and adjusts accordingly.

      The card container has also been used to display the day's six time readings beneath the country/city weather metadata, which is responsive on all screen devices.

   2. The button

      1. Confirm that clicking the "Return Home" button on the page takes the user to the correct page.

         When tested on all devices, the user is directed back to the home page as expected if they click the "Return Home" button.
      

#### **DELETE MODAL**
**( Delete Sensor)**

1. Ensure that when the "delete" link on the result page is clicked, a modal window appears asking the user to confirm their action.

      The modal appears when the user clicks the "delete" link located beneath the "return home" button when tested across all devices. A dialogue box appears, asking the user to confirm that they want to perform the desired function. When the user clicks the delete button, the sensor is removed from the website's database.


2. Ensure that clicking the "Cancel" link returns the user to the correct page.
      When tested on all devices, the cancel button returns the user to the home page and the dialogue box disappears.
      However, due to time constraints, it was not possible to link the sensor id to the cancel button to allow the user to return to the result page, so the home link was used in the cancel button instead.

<br/>

### **FURTHER TESTING** 
When running the tests for the form in the weather app, an error was discovered that prevented the test from running. The error "missing 1 required argument:'self'" occurred because I forgot to provide a required argument when instantiating the Sensor class that was added to the sensor model. 

After that, another error message appeared: "__init__() missing 1 required positional argument: 'city name" The arguments for the initiated class were present in all three of the sensor data, but when attempting to set the values to default, another error "test city name is required() missing 1 required positional argument:'self'" appears. After some research, and due to time constraints, testing for the views.py and models.py files was omitted because it would have necessitated more debugging.


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

*  Allow for more unit testing on the weather app, as well as the addition of more data that can be stored and manipulated.

* Include a button on the single view page that allows the user to view the day's average temperature based on the time stamps provided for each sensor registered.

* If the user is logged in and can perform CRUD functions, they can save weather metadata in their database and update the values with real-time weather metadata from the API.

* Add restrictions in the Sensor Form to prevent duplicate forms of the same city and country name from being stored in the database, and to ensure that the city and country provided are actual places rather than just formed locations before registering.
