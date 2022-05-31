# Weather App Challenge

A weather app that retrieves sensor weather data for each country and city. If the user wants to see more weather details about a specific country, using the [Open Weather API](https://openweathermap.org/api) they can click the view more button to see the average temperature for the day.

Deployed site can be found [here](https://weathertabs.herokuapp.com/)

## Table of contents

[User Experience](#user-experience)

- [User Stories](#user-stories)
- [Styling](#styling)
  - [Colours](#colours)
  - [Fonts](#fonts)

[Features](#features)

- [Implemented](#implemented)

[Technologies used](#technologies-used)

- [Languages](#languages)
- [Libraries](#libraries)
- [Programs and tools](#programs-and-tools)
- [JS Tools Installed](#js-tools-installed)

  - [npm](#npm)
  - [Prettier](#pretier)
  - [ESLint](#eslint)
  - [Git](#git)
  - [Parcel](#parcel)
  - [Babel](#babel)
  - [React](#react)

- [Structure](#structure)
  - [Components](#components)
  - [Css](#css)

# **Table of Contents**   
1. [UX Development](#ux-development)
     
    * [USER STORIES](#user-stories)
        * [New User/Returning Users](#new-user-or-returning-users)

   * [DESIGN](#design)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Database Structure](#database-structure)
        
2. [Features](#features)  
    * [General Features On All Pages](#general-features-on-all-pages)
    * [Features To Implement In Future](#features-to-implement-in-future)
      
3. [Technology Used](#technology-used)  
    * [Language Used](#language-used) 
    * [Frameworks & libraries](#frameworks-libraries)
    * [Packages/Dependencies Installed](#packages-dependencies-installed)
    * [Database Management](#database-management)
    * [Storage & Hosting](#storage-hosting)


4. [Testing](#testing)   
    * [TEST.md](#testing)   

5. [DEPLOYMENT](#deployment)
    * [How to Use Project](#how-to-use-project)
    * [Project Set Up](#project-set-up)
    * [Deployment To Heroku](#deployment-to-heroku)

7. [Credits](#credits)  
    * [Content](#content) 
    * [Media](#media)  
 
8. [Acknowledgements](#acknowledgements)  

# **UX Development**   
### **USER STORIES**
#### **NEW USER OR RETURNING USERS**
As a new user/ registered shopper, I want to:
1.	Be able to find weather information easier. 
2.	Be able to save Country and City data in order to easily access more weather information about a saved city. 
3.  Be able to delete Country and City data along with its metadata. 

## **DESIGN**   
### **Color Scheme**  
The colours used in the design for the  Weather App was blue. The colour was inspired by the sky in order for the user to intuitively understand the purpose of the site. 

### **Typography**  
The [Google Fonts](https://fonts.google.com) Quicksand has been used to give the site a clean a friendly clean minimalist design.

# **Features**  
## **Existing Features** 

### **GENERAL FEATURES ON ALL PAGES :**  
   - **Fully Responsive**: Each page is fully responsive across all devices and has been designed to be user-friendly and intuitive.

   - **Navigation Bar** - There is a fully responsive navigation bar on all pages. 

   - **Modal** - On the single view page , a modal appears to allow the user to conduct basic operations such as deleting a sensor data. When the admin user wants to conduct any delete functionality, a popup appears to verify their action.

### **FEATURES OF EACH PAGE**     

#### **1. Home Page**

When visiting the weather app page, the user can enter both the country name and the city name to find their sensor metdata. When a user adds a sensor, the homepage displays all of the sensors.

The site has been kept clean in order for users to easily navigate and interact with it. To draw the user's attention, the header phrase, which welcomes the user to the site, is placed in the center of the site.
   <br/>

#### **2. Single View Page**

The page displays more detailed weather metdata for each sensor.
- It contains the following elements: the sensor image for the country, the weather temperature for the same day with minimum and maximum temperatures. In addition, wind, humidity, and temperature data are provided.

   <br/>  

# **Technology Used**
### **LANGUAGE USED** 
   * [HTML5](https://en.wikipedia.org/wiki/HTML5)   
   * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)     
   * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))   

### **FRAMEWORKS & LIBRARIES**   
   * [Django Template](https://jinja.palletsprojects.com) : Django used this as a templating language to display backend data on the frontend.

   * [BOOTSTRAP 4.0](https://getbootstrap.com/docs/5.0/):  This was used to help with the website's structure, style, and responsiveness across all devices.

   * [Fontawesome](https://fontawesome.com/) : This was used to convey information using icons and to improve the site's appearance.

   * [Google Fonts](https://fonts.google.com/) : For this project's design, the font Quicksand has been imported into the stylesheet.

   * [GITHUB](https://github.com/) : This was the location of the project's code.


### **PACKAGES/ DEPENDENCIES INSTALLED**

   * [Gunicorn](https://gunicorn.org/) : This is an HTTP server for WSGI applications that will be used to aid in the deployment of the project.


### **DATABASE MANAGEMENT**

   * [SQLite](https://www.sqlite.com/index.html) : This served as our database for development.  

   * [Heroku Postgres](https://www.heroku.com/postgres) :  This was used for our Heroku database in production.  

### **PAYMENT SERVICE** 
   * [Stripe]https://dashboard.stripe.com/): This was used to process payments on the website. 

### **STORAGE & HOSTING**  
   * [Whitenoise](http://whitenoise.evans.io/en/stable/) :This was used in production to serve our static files, making it a self-contained unit that can be deployed anywhere.

   * [Heroku](https://en.wikipedia.org/wiki/Heroku) : This was our preferred cloud platform for deploying our project.

   * [GITHUB](https://github.com/) : This was our preferred cloud platform for deploying our project.

### **OTHER TOOLS**  

   * [GIT](https://git-scm.com/) : This was the preferred method of version control. To commit and publish our project to GitHub, we used the gitpod. 

   * [PEP8](http://pep8online.com/) : This was used to run our Python code to ensure it was free of errors.

   * [CHROME DEV TOOLS]() : This was used to test the responsiveness of our website across different screen sizes.

   * [dbdiagram.io](dbdiagram.io) : This was used to create the MMÀ- HAIRCARE database schema. 

   * [Adobe Color](https://color.adobe.com/): This was used to select the site's colour scheme.

   * [TinyPNG](https://tinyjpg.com/): This is an image compressor that is used to compress all images.


  