# **TOODLE**

![Mock up](wireframes/#)


## **Goal for this project**


In the fast pace world it's really easy to get overwhelemed with the number of thing we need to do. 
This project is an attempt to make organising and going though your to do list easier.

Whether you want to break your big overwhelming tasks into smaller more managible tasks or organise
you College, Home, Personal activities and have your tasks in organised different lists categories that you set
Toodle you personal to do list organiser is here at your service.
 


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
* [Wireframes](#wireframes-and-flowcharts)
    * [Wireframes](#wireframes)
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
* [Code Sources Used/References](#code-sources)
* [Credits](#credits)

--- 

<a name="ux"></a>

## **UX**

<a></a>

### **User Goals**

* The website has to work well on all kind of devices like mobile phones, tables and desktops.
* I want to have a clear dashboard where I can see all my list categories displaid and with the tasks assigned to them
* I want to have an option to create my personalised list categories
* I would like to easily add and remove to do list items from the list
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
* As a user, I want to have the possibilty to delete a list when is no longer relevant
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
* Easy way to add/remove items to to do lists
* Easy way to add new to do list category
* Ability to edit and delete existing list items/lists

<a></a>

#### Expectations

* Ability organise my to do list
* Easy to add my tasks to my list
* Personalised profile 
* My information is saved when I can add it

[Back to Top](#table-of-contents)

<a></a>

### **Design Choices**

I wanted to use landing page to introduce the user to the benifits of using to do list and organising your activities.
To get the efect I wanted I decided to use Start Bootstrap template, the image of the post it notes scaterred on the wall 
with the tasks illustrating the start of organising the chaos of the to do list and I believe carries out the task perfecly.
The landing page is informative listing benifits of having a to do list and it calls for action to Sign Up for the page or Log In with existing details.

My goal was to keep the color palet simple and clean. 

<a></a>

#### Colors



* #ffffff: I have decided to keep the background of the overall website white in order give the clean look. This color is used for text color for the nav bar and buttons.
* #2a9d8f: Navigation bar and buttons



<a></a>

#### Fonts
I used  [Google Fonts](https://fonts.google.com/ "Google Fonts") to find the fonts to use.


<a></a>

#### Structure

As I mention before I took the landing page template from [StartBootrap](www.startbootstrap.com). It created lovely welcome page
with useful information, points and benifits of to do lists. Then the rest of the website I chose to use [Materialize](https://materializecss.com/), because
 I really enjoyed the different components and the depth different materials create for the website.

[Back to Top](#table-of-contents)

--- 
<a></a>

## **Wireframes**

### **Wireframes**
 [Balsamic](https://balsamiq.com/wireframes/) programme was used to create wireframes for my website: 


#### Desktop Wireframes
* [Dashboard](wireframes/desktop.pdf)


#### Tablet Wireframes
* [Dashboard](wireframes/tablet.pdf)


#### Mobile Wireframes
* [Dashboard](wireframes/mobile.pdf)



### **Database Structure**

MongoDB was used to set up the database for this project with the following collections: 

#### **Users:**

Key      | Value
---------|-----------
_id      | ObjectId
username | String
password | String

#### **List Categiories:**

Key             | Value
----------------|-----------
_id             | ObjectId
user_id         | String
list_name       | String
list_image      | String

#### **List Items:**

Key             | Value
----------------|-----------
_id             | ObjectId
user_id         | String
list_id         | String
list_item       | String



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
    * Create: new personalised list categories 
    * Read: list disppay where you can view all the created lists categories and tasks added to them 
    * Update: possibility to update categories
    * Delete: possibility to delete tasks from the lists, delete categories

<a></a>

### **Features to be implemented**

* I would like to add functionality that helps sort out the tasks by date
* I would like to have a seperate tab just for todays tasks
* I would lke to add differnrt fileters to allow the user customise their own list in the way they prefer, whether it by the date
or category 
* I would like to add Search Functionality 

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

2. Access the folder in your terminal window and install the application's [required modules](https://github.com/dovi-k/toodle/blob/master/requirements.txt) using the following command:

    ```
    pip3 install -r requirements.txt
    ```

3. Sign-in or sign-up to [MongoDB](https://www.mongodb.com/) and create a new cluster
    * In the Sandbox, click the collections button and after click Create Database 
    * Set up the following collections: users, lists, lists_category

    * Under the Security Menu on the left, select Database Access.
    * Add a new database user, and keep the credentials secure
    * Within the Network Access option, add IP Address 0.0.0.0

4. In your IDE, create an env.py file containing your environmental variables at the root level of the application. 
    Containing the following lines and variables:
    ```
    import os

    os.environ["IP"] = "0.0.0.0"
    os.environ["PORT"] = "5000"
    os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"
    os.environ["DEBUG"] = "True"
    os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"
    os.environ["MONGO_DBNAME"]= "DATABASE_NAME" 
    ```
.
    Make sure env.py file is added to .gitignore file before pushing to your GitHub repository.

5. The application can now be run locally. In your terminal, type the following command 
    ```
    python3 app.py. 
    ```
    
### Steps to Deploy your project to Heroku: 

1. Sign up for Heroku account or Login to your existing account. 
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

## **Code Sources/References**

I used a lot of code from different sources to support my project. I used a lot of Code from Course Miniproject to the point
where one week before the submission I was advised that it may be too similar to the Miniproject. My project theme it being a to do list
was not helping as well, miniproject was as well using the Materialise library.
So I continued on working on my To Do list app "Toodle" in hopes to hopefully upgrade it but I end up running out of time 
and didn't managed to implement a lot of upgrades I wished I could.

## Code References
* to create a functioning to do list I refenced and used code from these Youtube Tutorials
[Code Explained To Do List App in JS](https://www.youtube.com/watch?v=b8sUhU_eq3g&t=5s) and most of the code from 
[SabCode To Do List](https://www.youtube.com/watch?v=GQTtbVuy1UY&t=37s) for the To Do lists to be displayed
* Landing page from [StartBootsrap Landing-page theme](https://startbootstrap.com/theme/landing-page), I used different images,
customised colours, icons and text
* Most of the styling comes from [Materialize](https://materializecss.com/), teal colour, shadow, nav bar, input fields
* When creating Functions and interactions with Mongo DB I was referencing a lot Code Institute Task Manager Miniproject
followed the sign up, sign up functions and made them work for my page
* ReadMe file Stucture was based from Anouk Smet project [Dogs Health Tracker](https://github.com/AnoukSmet/Dog-Health-Tracker/blob/master/README.md#testing)
* Images for the website taken from [Pexels](https://www.pexels.com/search/to%20do%20list/)


## **Credits**

* I would like to thank my mentor Simen [Eventyret_mentor](https://github.com/Eventyret) for his patiance and support though a ver!
* I want to thank my workmate and fellow student [Irina](https://github.com/irinatu17) for inspiration and suppport
* I want to thank the [Stackoverflow](https://stackoverflow.com/) community as well as [Code Institute](codeinstitute.ie) Slack community
* I would like to thank Code Institute Student care for support.

[Back to Top](#table-of-contents)




