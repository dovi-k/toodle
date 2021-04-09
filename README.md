# **TOODLE**

![Mock up](wireframes/#)


## **Goal for this project**


In the fast pace world it's really easy to get overwhelemed with the number of thing we need to do. 
This project is an attempt to make organising and going though your to do list easier.

Making to do list is proven to 
 


--- 

<a></a>

## Table of contents 
* [UX](#ux)
    * [User Goals](#user-goals)
    * [User Stories](#user-stories)
    * [Site Owners Goals](#site-owners-goals)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
        * [Requirements](#requirements)
        * [Expectations](#expectations)
    * [Design Choices](#design-choices)
        * [Fonts](#fonts)
        * [Colors](#colors)
        * [Structure](#structure)
* [Wireframes and Flowcharts](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
    * [Flowcharts](#flowcharts)
    * [Database Structure](#database-structure)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Features to be implemented](#features-to-be-implemented)
* [Technologies used](#technologies-used)
    * [Languages](#languages)
    * [Libraries and Frameworks](#libraries-and-frameworks)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Heroku Deployment](#heroku-deployment)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

* The website has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a clear dashboard where I can see all the different logs I have created. 
* The log should appear with the most recent one on top to be relevant. 
* I want to have a profile for my dog where I can enter information like the name, breed etc. 
* I would like to have the option to add multiple dogs
* The website has to be easy to use and easy to update information
* Visually appealing website

[Back to Top](#table-of-contents)

<a></a>

### **User Stories**

* As a user, I would like to be able to register for the website so I can have my personal environment.
* As a user, I want to be able to easily organise activities I need to do in a list
* As a user, I want to login after I created an account and see my previous inserted information.
* As a user, I would like to have a personal profile 
* As a user, I want to be able to make a multiple lists 
* As a user, I want to be able to edit my list
* As a user, I want to have the possibilty to delete a log as well when no longer relevant. 
* As a user, I want the website to be easy to use. 


<a></a>

### **Site owners Goals**
* To have an appealing website that users can organise their day to day activities
* To have a great user friendly design and functionality  


[Back to Top](#table-of-contents)

<a></a>

### **User Requirements and Expectations**

<a></a>

#### Requirements

* Easy to navigate by using the few buttons
* Easy way to add items to to do lists
* Easy way to add new to do list
* Ability to edit and delete existing list items/lists

<a></a>

#### Expectations

* Ability organise my to do list
* To have a dashboard where all the necessary information is visible
* Easy to add my tasks to my list
* Personalised profile 
* My information is saved when I can add it

[Back to Top](#table-of-contents)

<a></a>

### **Design Choices**

I wanted to use landing page to introduce the user to the benifits of using to do list and organising your activities.
To get the efect I wanted I decided to use Start Bootstrap template, the image of the post it notes scaterred on the wall 
with the tasks illustrating the start of organising the chaos of the to do list and I belive carries out the task perfecly.
The landing page is informative and it calls for action to Sign Up for the page or Log In with existing details.

The Colors I have used are 

I wanted to keep the color palet simple and clean. 

I have used [Coolors](https://coolors.co/ "Coolors.co") to come up with a color scheme that matches the atmosphere of a Health Tracker.
For this website I have deciced to keep design simple, meaning I opted for a white background color with some light gray for the profile and logs.
I have added some color (blue) for the buttons, navigation bar and footer to make the design more visually appealing to the user. 
The reason for this is that for this project, the functionality is much more important and as there are a lot of functionalities I don't want to distract the user with overwhelming colors. 

<a></a>

#### Colors

Like I mentioned before, I have decided to use some colors that fit well with the feeling of a Health Tracker.
Below I will explain more why I choose the various colors and for what I will be using them.

![Color Palette](wireframes/color-palette.png)

* #ffffff: I have decided to keep the background of the overall website white in order give the clean look. I will also use this color as text color for the nav bar and buttons.
* #D9D9D9: This color I will use as a background color for whole dashboard. 
* #F5F5F5: This color I will use as a background color for the logs on the dashboard in order to have a small contract versus #D9D9D9 dashboard color.
* #284B63: This will be the color that I will use for my navigation bar and buttons in order to give a bit of color to the website. This color will also be used as the overall text color.

I have used a contrast checker in order to make sure that the contrast is sufficient.
This way my content will be easily readable. 

<a></a>

#### Fonts
In order to find appropriate fonts for my website, I have visited [Google Fonts](https://fonts.google.com/ "Google Fonts") to explore the various options.
For the titles and subtitles, I have used the font [Play](https://fonts.google.com/specimen/Play "Play") 
and for the main text I have used [Cormorant Garamond](https://fonts.google.com/specimen/Cormorant+Garamond "Cormorant Garamond"). 

<a></a>

#### Structure

I have chosen to use [Materialize](https://materializecss.com/) to create an overall structure for my website. 
Materialize provides various elements of CSS and Javascript which is very helpful to keep a good structure on your page. 
The reason why I choose Materiaize is mainly due to the various features they offer like a datepicker, floating action button etc. 

[Back to Top](#table-of-contents)

--- 
<a></a>

## **Wireframes and Flowcharts**

### **Wireframes**
I used [Balsamic](https://balsamiq.com/wireframes/) to create wireframes for my website. 

You can find my wireframes below:

For the homepage I have only created 1 wireframe as the design is quite basic and looks identical on all screen sizes.
* [Home](wireframes/desktop-home.png)

#### Desktop Wireframes
* [Dashboard](wireframes/desktop-dashboard.png)
* [Add Dog](wireframes/desktop-adddog.png)
* [Add Log](wireframes/desktop-addlog.png)

#### Tablet Wireframes
* [Dashboard](wireframes/tablet-dashboard.png)
* [Add Dog](wireframes/tablet-adddog.png)
* [Add Log](wireframes/tablet-addlog.png)

#### Mobile Wireframes
* [Dashboard](wireframes/mobile-dashboard.png)
* [Add Dog](wireframes/mobile-adddog.png)
* [Add Log](wireframes/mobile-addlog.png)

### **Flowcharts**

I have decided to make a flowchart for the sign-in / register proccess to completely understand each step of the process.  
I have used [Draw.io](https://draw.io/) to make this flowchart which you can view below: 

[Flowchart](wireframes/flowchart.png)

### **Database Structure**

I have used MongoDB to set up the database for this project with the following collections: 

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### **Dogs:**

Key             | Value
----------------|-----------
_id             | ObjectId
user_id         | String
dog_name        | String
dog_breed       | String
date_of_birth   | String
dog_description | String
dog_image       | String

#### **Logs:**

Key             | Value
----------------|-----------
_id             | ObjectId
dog_id          | String
user_id         | String
log_date        | String
dog_weight      | String
weight_metric   | String
dog_activity    | String
dog_food        | String
food_metric     | String
other_notes     | String

#### **Food_metrics** ####

Key             | Value
----------------|-----------
_id             | ObjectId
metric_name     | String

#### **Weight_metrics** ####

Key             | Value
----------------|-----------
_id             | ObjectId
metric_name     | String


[Back to Top](#table-of-contents)

---

<a></a>

## **Features**

<a></a>

### **Existing Features**

* Registration functionality
* Sign-In and Out functionality
* Add multiple dogs per user 
* CRUD Functions:
    * Create: possibility to add various dogs and logs
    * Read: dashboard where you can view the dog profile(which was selected) and its logs
    * Update: possibility to update the dog profile and logs
    * Delete: possibility to delete the dog profiles and logs
* Search logs by log date

<a></a>

### **Features to be implemented**

* Currently the user can only insert image url. In the future I would like that the user can upload an image from its computer and/or cloud accounts.
* Have a more extensive user profile with, profile image, preferences and email to which you can send updates, newsletters etc.
* Have a 'forget password' functionality.
* Include a confirm password to make sure the user has chosen the password he/she wanted. 
* Possibility for the user to be able to add (and remove) categories they would like to specificely track for their dog like medication etc. 
* The possibility to filter the logs based on range of data or by month.
* Expand search function so user can filter on more keywords except for log_date.
* Submit search form as soon as the user selected a date to prevent confusion for the user. (Did I already click search or not)
* Add pagination so the list of logs will be display with a max of 20 logs per page.
* When the user has added their first log, I would like to remember the chosen metrics for any futher logs so they don't have to update this every time they add a log.
    This would be done through profile preferences or store the data in a cookie. 
* Give the user the possibility to add a 'Picture of the day' to the log and display it on the dashboard.
* Add a graph overview page, especially for the tracking of the weight with nice visual aspect.

[Back to Top](#table-of-contents)

<a></a>

## **Technologies used**

<a></a>

### **Languages**

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://www.python.org/)

<a></a>

### **Libraries and Frameworks**

* [Font Awesome](https://fontawesome.com/)
* [Materialize](https://materializecss.com/)
* [Google Fonts](https://fonts.google.com/)
* [jQuery](https://jquery.com/)
* [StartBootrap](https://startbootstrap.com/)

### **Tools**
* [Git](https://git-scm.com/)
* [GitPod](https://www.gitpod.io/)
* [Heroku](https://www.heroku.com/)
* [Balsamic](https://balsamiq.com/wireframes/)
* [W3C HTML Validation Service](https://validator.w3.org/)
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)
* [MongoDB Atlas](https://www.mongodb.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [PyMongo](https://api.mongodb.com/python/current/tutorial.html)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

[Back to Top](#table-of-contents)

<a></a>

## **Deployment**

### Local Deployment

Toodle has been created using [Github][github.com] and from there [Gitpod](https://gitpod.io/) for my code.

Gitpod was used for development and following steps are going to be refering to this specific IDE.


#### Cloning Toodle: 

1. Select application repository, select CODE button. That will dowload the zip of the repository

Link to the repository:
    ``` 
    https://github.com/dovi-k/toodle
    ``` 

1. Access the folder in your terminal window and install the application's [required modules](https://github.com/dovi-k/toodle/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

1. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * Within the Sandbox, click the collections button and after click Create Database (Add My Own Data) called dog_health_tracker
    * Set up the following collections: users, dogs, logs, food_metrics and weight [Click here to see the exact Database Structure](#database-structure)
    * Under ***food_metrics*** and ***weight_metrics***, add your preferred metrics in the collection with the following structure: 
        ```
        Key             | Value
        ----------------|-----------
        _id             | ObjectId          This will be automatically generated by MongoDB
        metric_name     | String            Replace string by kg, pounds, grams, ounces etc.
        ```

    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

1. In your IDE, create a file containing your environmental variables called env.py at the root level of the application. 
    It will need to contain the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```

    Please note that you will need to update the **SECRET_KEY** with your own secret key, as well as the **MONGO_URI** and **MONGO_DBNAME** variables with those provided by MongoDB.
    Tip for your SECRET_KEY, you can use a [Password Generator](https://passwordsgenerator.net/) in order to have a secure secret key. 
    I personlly recommend a length of 24 characters and exclude Symbols.
    To find your MONGO_URI, go to your clusters and click on connect. Choose connect your application and copy the link provided. 
    Don't forget to update the necessary fields like password and database name. 

    If you plan on pushing this application to a public repository, ensure that env.py is added to your .gitignore file.

1. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
    
### Steps to Deploy your project to Heroku: 

1. Sign up for Heroku accoun or Login to your existing account. 
On your dashboard top right corner press New->Create a new app. Choose region closest to you and name the app.
2. Create the Procfile and requirements.txt files. Make sure requirements.txt is up-to-date in your local repository.  
    Requirements:
    ```
    pip3 freeze --local > requirements.txt
    ```
    Procfile:
    ```
    echo web: python app.py > Procfile
    ```
3.  Procfile should contain the following line and no new line in the end as that could cause issues in the deployment:
    ```
    web: python app.py
    ```

4. Open the app Dashboard->Deployment tab->scroll to "Deployment methods". Click on GitHub for automatic deployments.
 Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.

5. From the bellow "App connected to Github" section make sure your github user is selected in the inputs, 
and then enter the name for your repo. Click "search". When it finds the repository, click the "connect" button.

6. At the top of dashboard nav bar click on "settings". Scroll down and click "Reveal config vars". 
Set up the same variables as in your env.py (IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME):
    !It's better not to set the DEBUG variable in under config vars and use it only in your env.py to prevent DEBUG being active on live website. 

    ```
    IP = 0.0.0.0
    PORT = 5000
    SECRET_KEY = YOUR_SECRET_KEY
    MONGO_URI = YOUR_MONGODB_URI
    MONGO_DBNAME = DATABASE_NAME
    ```

7. Scroll back up and click "Deploy" on the Nav bar. Scroll down to "Automatic Deploys" section 
and click "Enable automatic deployment".

8. Slightly bellow at the "Manual Deployment section" click "Deploy branch". 
Heroku will start building the app. When the build is complete you can click "view app" to open it.

9. In order to commit your changes to the branch, use git push to push your changes. 
    

[Back to Top](#table-of-contents)

<a></a>

## **Credits**

* I would like to thank my mentor Simen [Eventyret_mentor](https://github.com/Eventyret) for his patiance and support though a ver!
* I want to thank my workmate and fellow student [Irina](https://github.com/irinatu17) for inspiration and suppport
* I want to thank the [Stackoverflow](https://stackoverflow.com/) community as well as [Code Institute](codeinstitute.ie) Slack community

[Back to Top](#table-of-contents)




