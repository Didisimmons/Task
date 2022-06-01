# Weather Tabs 

A weather app that retrieves sensor weather data for each country and city. If the user wants to see more weather details about a specific country, using the [Open Weather API](https://openweathermap.org/api) they can click the view more button to see the various temperature for the day of that sensor.

Deployed site can be found [here](https://weathertabs.herokuapp.com/)

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
    * [Structure](#structure)
      
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


# **UX Development**   
### **USER STORIES**
#### **NEW USER OR RETURNING USERS**
As a new user/ registered user, I want to:
1.	Be able to find weather information easier. 
2.	Be able to save Country and City data in order to easily access more weather information about a saved city. 
3. Be able to delete Country and City data along with its metadata. 

## **DESIGN**   
### **Color Scheme**  
The colours used in the design for the  Weather App was blue. The colour was inspired by the sky in order for the user to intuitively understand the purpose of the site. 

### **Typography**  
The [Google Fonts](https://fonts.google.com) Quicksand has been used to give the site a clean a friendly minimalist design.

# **Features**  
## **Existing Features** 

### **GENERAL FEATURES ON ALL PAGES :**  
   - **Fully Responsive**: Each page is fully responsive across all devices and has been designed to be user-friendly and intuitive.

   - **Navigation Bar** - There is a fully responsive navigation bar on all pages. 

   - **Modal** - On the single view page , a modal appears to allow the user to conduct basic operations such as deleting a sensor data. When the admin user wants to conduct any delete functionality, a popup appears to verify their action.

### **FEATURES OF EACH PAGE**     

#### **1. Home Page**

When visiting the weather app page, the user can enter both the country name and the city name to find their sensor metdata. When a user adds a sensor, the homepage displays all of the sensors.

The site has been kept clean in order for users to easily navigate and interact with it. To draw the user's attention, the header phrase, which welcomes the user to the site, is placed at the center of the site.
   <br/>

#### **2. Single View Page**

The page displays more detailed weather metadata for each sensor.
- It contains the following elements: the sensor icon for the country, the weather temperature for the same day with minimum and maximum temperatures. In addition, wind, humidity, and temperature data are provided.


### **FEATURES TO IMPLEMENT IN FUTURE**  

*  **Toast Messages**: Currently, the user is not notified when they perform an action, but it would be nice to add toast messages to alert users about their action on the site for a better user experience.

*  **User accounts**: Currently, anyone who can access the site can perform some basic CRUD functions such as adding and deleting sensors. It would be ideal if each user could create their own account and register their preferred sensor. The user only needs to edit and delete their sensors to be able to retrieve live data for each sensor. There should also be some defensive programming that allows the admin user to access features that the registered user does not have access to.


### **STRUCTURE**  

Some pieces of the code were resused in order to fetch data from Weather API. 

- App : This is an app that allows the user to register a sensor with information like "country name" and "city name." When this information is entered, the form is sent to the database, which stores the new sensor. The newly saved sensor data is used to invoke the open weather API, which retrieves the most recent weather metadata for that sensor and attaches it to the sensor displayed on the homepage.

If the user wants to see more metadata about a sensor, they can do so by clicking the view more button. This selects the sensor's id and also calls the open weather API to retrieve weather updates of the metadata for that sensor id  and display data for the user.

The user can also delete sensor data by clicking the delete link, which launches a modal on the single view page. The user is asked to confirm their decision; if they do, the sensor id and its data are deleted, and the user is returned to the home page.

<br/>  

# **Technology Used**
### **LANGUAGE USED** 
   * [HTML5](https://en.wikipedia.org/wiki/HTML5)   
   * [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)     
   * [Python](https://en.wikipedia.org/wiki/Python_(programming_language))   

### **FRAMEWORKS & LIBRARIES**   
   * [Django Template](https://jinja.palletsprojects.com) : Django used this as a templating language to display backend data on the frontend.

   * [BOOTSTRAP 5.0](https://getbootstrap.com/docs/5.0/):  This was used to help with the website's structure, style, and responsiveness across all devices.

   * [Fontawesome](https://fontawesome.com/) : This was used to convey information using icons and to improve the site's appearance.

   * [Google Fonts](https://fonts.google.com/) : For this project's design, the font Quicksand has been imported into the stylesheet.

   * [GITHUB](https://github.com/) : This was the location of the project's code.

   * [Open Weather](https://openweathermap.org/api/) : This was used to fetch live weather foorecast updates for each country and city. 

### **PACKAGES/ DEPENDENCIES INSTALLED**

   * [Gunicorn](https://gunicorn.org/) : This is an HTTP server for WSGI applications that will be used to aid in the deployment of the project.


### **DATABASE MANAGEMENT**

   * [SQLite](https://www.sqlite.com/index.html) : This served as our database for development.  

   * [Heroku Postgres](https://www.heroku.com/postgres) :  This was used for our Heroku database in production.  

### **STORAGE & HOSTING**  
   * [Whitenoise](http://whitenoise.evans.io/en/stable/) :This was used in production to serve our static files, making it a self-contained unit that can be deployed anywhere.

   * [Heroku](https://en.wikipedia.org/wiki/Heroku) : This was our preferred cloud platform for deploying our project.

   * [GITHUB](https://github.com/) : This was our preferred cloud platform for deploying our project.

### **OTHER TOOLS**  

   * [GIT](https://git-scm.com/) : This was the preferred method of version control. To commit and publish our project to GitHub, we used the gitpod. 

   * [PEP8](http://pep8online.com/) : This was used to run our Python code to ensure it was free of errors.

   * [CHROME DEV TOOLS]() : This was used to test the responsiveness of our website across different screen sizes.
 

  # **Testing**  
The testing documentation can be found [here](TEST.md). 

<br/>  

# **DEPLOYMENT**   
This project was created with Gitpod as the IDE, committed to git as its local repository, and is hosted on Github. The project is deployed using a free hosting service (Heroku).

To Deploy Weather App the following are needed 
   -	A Heroku account  
   -	A github account 


### **How To Use Project**   
In the event that a user wishes to fork the project or clone the project, the necessary steps are also provided below.

#### **Forking the repository**  
1. Sign in to your GitHub account.  
2. Locate the repository to be duplicated, in this case Task.  
3. Locate and click the “Fork” button at the top of the  Task. 
4. This creates a copy of the repository in our account and allows us to make changes.

#### **Making A Local Clone of Github Repository**   

1. Locate the desired repository in this case Task, under the repository name click Clone or download.

2. Click it and copy the HTTPS link that appears.

3.	Activate your local IDE terminal.

4.	Change the current working directory to the location where you wish the cloned file to be saved.

5.	In the terminal, type “git clone” and then paste the link copied from HTTPS.  
```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```

6. Press Enter and  your local clone is created.

7. Create a new env.py file in the base directory and include the following code.
```
import os
#Django
os.environ.setdefault( 'DEVELOPMENT', 'True')
os.environ.setdefault('SECRET_KEY', '<YOUR_KEY>')

```
8. Ensure that the env.py file is located in the .gitignore file.

9. Type the following into the terminal to install our required dependencies and modules.
      ```pip3 install -r requirements.txt```


#### **Project Set Up** 
After forking or cloning the Task repository, the following steps must be completed in order for our github repository to be deployed to Heroku.
1.  Ensure that all WeatherApp dependencies are installed and operational. The gitignore file contains all of the necessary hidden files.

2. Go to your gitpod workspace after installing the necessary dependencies. Variables can be found under Settings - --> Variables. Enter the following project environment variables:
   Varables | Key   
   ---| ---   
   DEVELOPMENT | TRUE   
   SECRET_KEY | <your_secret_key>  

   These keys can be obtained from  
      -	The SECRET_KEY from [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) 

3. Make migrations to keep our database up to date.

4. We can now run the server and deploy after it has been updated.

### **Deployment To Heroku**

1. Create a new Heroku App
   - Sign in or create a Heroku account. After logging in, click "Create new app" in the top right corner of your dashboard.

   - Give your app a unique name and use a hyphen between words.

   - Select a region near you and then click Create App.

2. Navigate to the resources tab on the app dashboard, search for "Heroku Postgres" under Add-ons, select it, and then select the free plan.

3. On Heroku's Dashboard, Under settings, click the "Reveal Configure vars" button and enter the required configuration variables, including those whose values may not yet be present. The unavailable values would be updated as you progress through the steps.
      Varables | Key   
      ---| ---   
      DATABASE_URL| Your database url 
      SECRET_KEY | Your secret key

4. Return to your project's Gitpod IDE and use the CLI to install the following important files: 
   ```
   pip3 install dj_database_url
   pip3 install psycopg2-binary
   ```
   - Once the requirements have been created, we must freeze them in our CLI ``` pip3 freeze > requirements.txt ```to ensure that Heroku instals our app when it is deployed.

   - Create a new database for WeatherApp by importing dj database url into our settings.py file and commenting out our default configuration. We would need to replace the default database with a call to dj database url.parse and pass it the database URL from Heroku (which can be found in our app settings tab's config variables).
      ```
      DATABASES = {
      'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
      }
      ```
   - Run migrations
      ```
      python3 manage.py migrate
      ```

5. Create a new super user to log in with and provide details for the username and password.
   ```
   python3 manage.py create superuser
   ```

6. Remove the Heroku database URL from our settings.py file and uncomment the default database configuration. Add an if statement to specify that if the app is running on Heroku, it should connect to Postgres; otherwise, it should connect to Sqlite.

    ```
    if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    ```  

7. Once we've created our conditional statement, we'll need to install Gunicorn, which will serve as our webserver.  
   ```
   pip3 install gunicorn 
   ```

8. Freeze our requirements after installation to ensure that all of our app's required packages are installed.
   ```
   pip3 freeze > requirements.txt 
   ```

9. Create a Procfile that instructs Heroku to create a web dyno that will run gunicorn and our app.
   ```
   web: gunicorn appname.wsgi:application 
   ```
10. Log in to Heroku via the CLI and temporarily disable collectstatic so that Heroku does not attempt to collectstatic files when it deploys.
   ```
   heroku config:set DISABLE_COLLECTSTATIC=1 --app appname
   ```

11. To store our static files and making it a self contained unit for deployment. Install whitenoise 
```pip install whitenoise ```

12.  In the settings.py file middleware section (at the top) add 

   ```
      MIDDLEWARE_CLASSES = (
      'whitenoise.middleware.WhiteNoiseMiddleware',
      )
   ```
13. Also in the settings.py file add 

``` STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' ```

14. After we have completed the preceding steps, we must add the hostname of our Heroku app (Weathertabs) to the list of allowed hosts in our settings.py and also include localhost so that Gitpod can continue to function:
   ```
   ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME', 'localhost')]
   ```

15. Save all files, commit, and push to github, then Heroku. We would need to initialise git remote because we created our app via the heroku  website rather than the terminal.
   ```
   heroku git:remote -a appname 
   ```
   and then push to Heroku using 
   ```
   git push heroku main 
   ```

16. Link our Git repository to Heroku
   - Return to the Heroku Dashboard and select "deploy" at the top.

   - Choose "GitHub" as the deployment method from the section.

   - This provides you with an input field in which you can search for your GitHub repository by name. When you find the correct repository, in our case "Task," click "Connect."

   - To ensure that all configuration variables on Heroku are updated with the required values, click the "Reveal Config Vars" button.


17. Enable Automatic Deployment

   - Once we've configured all of our environment variables, return to the dashboard and click "Deploy." Scroll down to "Automatic Deployments" and press the "Enable Automatic Deployment" button.

   - When we push to github, Heroku will automatically build our app with all of the required packages. Go to the top right corner and select "Open App" to view the website.

18. Return to our task-settings.py file and replace the secret key setting with the call to get it from the environment, with an empty string as the default.
``` SECRET_KEY = os.environ.get('SECRET_KEY') ```
