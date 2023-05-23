

<h1 align="center">Low Cholesterol Recipes</h1>


[View live project](https://low-cholesterol-food1.herokuapp.com/)


<img src="static/img/homescreen.png" width="400px">

"Low Chloestrol Recipes" -  Data-Centric  Milestone Project.

The purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) low cholesterol recipes. This gives access to all the recipes in the database for registered users. Registered users can add new recipes, edit and delete their own ones, as well as edit their username and password or delete there account.

# UX

My main goal in UX was to build a simple to use website where users can create their own recipes, view all the recipes, edit and delete their recipes. The target audience for this app is anyone who is looking for low cholesterol food.
This website has a user-friendly interface with easy access to all information. This app has been developed so registered users can easily add, delete and edit there own recipes with there own personal database.


# User Stories

As a user, I want:

1 .to view all recipe details which includes the name of the dish, meal, cooking time, servings, list of  ingredients and directions

2. to create my own account

3. to add new recipes


4. to edit and delete recipes on my account and all the recipes I've created

5. to view a list of my recipes on a separate page and see how many recipes I've created


6. to change my username and password

7. to delete my account and all recipes I've created

8. to have the ability to use the site on all modern browsers

9. to use the site on tablet , mobile or pc.

10. I want to be able to add in notes to each dish so I can add my own thoughts, experiences or
things I want to remember about cooking the dish.

11. I want the site to be easy navigate


# Design
The goal was to create a website that is overall user friendly, and providing information with the ability to create, read and delete the recipes. Therefore, following design choices were made:

## Framework
I chose Materialize for the front-end framework for this project.
JQuery was used for initializing some Materialize elements.

## Colour Scheme
The colour for the navbar is Cyan with the text being white with a slight text shadow.
The modals have an aqua colour, but when they are opened they have a white background.

## Typography
The font used is Playfair Display, serif

## Icons
I used FontAwesome as the main icon library across the project 

## Wireframes


## Features

The Navbar is not fixed, when you enter the website there 2 options , to login and register.
Once registered and logged in, there is a option to add a new recipe.
To view the recipes just click on the title Low Chloesterol food to view the recipes and within the recipe itself there is an option to edit and delete the recipe.In mobile, the links will display in a menu on the left hand side.

# Technologies Used

GitPod - an online IDE for developing this project.
Git - for version control.
GitHub - for remotely storing project's code.
PIP - for installation of necessary tools.
Am I Responsive - checking responsiveness.

## Front-End

HTML - to build the foundation of the project.
CSS - to create custom styles.

## Back-End

Python 3.8.2 - back-end programming language used in this project.
Flask 2.3.2 - microframework for building and rendering pages.
MongoDB - database for storing back-end data.
PyMongo 3.12.3 - for Python to get access the MongoDB database.


## Libraries

Materialize 1.0.0 - for front front-end framework.
FontAwesome - to provide icons used across the project.

## Testing
User stories testing
1 .to view all recipe details which includes the name of the dish, meal, cooking time, servings, list of ingredients and directions

2. to create my own account

3. to add new recipes

4. to edit and delete recipes on my account and all the recipes I've created

5. to view a list of my recipes on a separate page and see how many recipes I've created

6. to change my username and password

7. to delete my account and all recipes I've created

8. to have the ability to use the site on all modern browsers

9. to use the site on tablet , mobile or pc.

10. I want to be able to add in notes to each dish so I can add my own thoughts, experiences or
things I want to remember about cooking the dish.

11. I want the site to be easy navigate

validators , pep8 and python testing


# Compatibility and Responsiveness


# Bugs
I could not get postgres to work , I kept having the error:

psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory Is the server running locally and accepting connections on that socket?

Everything I tried did not work so I have decided to use MongoDB instead. I also had an error which was:

'Collection' object is not callable. If you meant to call the 'update' method on a 'Collection' object it is failing because no such method exists

This was related to the line mongo.db.starter.update({"_id": ObjectId(starter_id)}, edited_starter) in my edit_starters function in app.py, so I had downgrade pymongo from 4.3.3 to 3.12.3.

# Deployment
1. Set up environment variables.
Create .env file in the root directory.
On the top of the file, add import os to set the environment variables in the operating system
Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax: os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000") -
os.environ.setdefault("SECRET_KEY", "secret_key")
os.environ.setdefault("MONGO_URI", "")
os.environ.setdefault("MONGO_DBNAME", "mongo-dbname")

2. Install all requirements from the requirements.txt file putting this command into your terminal:
pip3 freeze --local > requirements.txt

3. Create a Procfile, which is what Heroku looks for to know which file runs the app, and how to
run it by using the following command in the terminal:
echo web: python run.py > Procfile

4.git add, git commmit and git push files.

5.Log into Herouku and create a new app, assign a name and select a region.

6.From the Heroku dashboard link the new Heroku app to your GitHub repository:
Click on Deploy followed by Github.
Make sure your GitHub profile is displayed, then add your repository name then click 'Search'.
Once it finds your repo, click to connect to this app.

7.Click on the 'Settings' tab for your app, and then click on 'Reveal Config Vars', where
we can securely tell Heroku which variables are required. Set the following vars:
IP : 0.0.0.0
PORT : 5000
SECRET_KEY : <your secret key>
MONGO_URI : <link to your MongoDB database: myfirst cluster > connect > drivers>
MONGO_DBNAME :  <link to your MongoDB database>


These are the same that are in the env file.

8.Enable Automatic Deployment on the deploy tab.

9.The app will be deployed and ready to run. Click "Open App" to view the app.








# Credits
