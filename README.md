

<h1 align="center">Low Cholesterol Recipes</h1>


[View live project](https://low-cholesterol-food1.herokuapp.com/)


<img src="test/homescreen.png" width="400px">

"Low Chloestrol Recipes" -  Data-Centric  Milestone Project.


The purpose of this full-stack MongoDB-based Flask project is to create a database of recipes that allows users to create, read, update and delete (CRUD) low cholesterol recipes. This gives access to all the recipes in the database for all users. Registered users can add new recipes, edit and delete their own recipes.

# UX

My main goal in UX was to build a simple to use website where users can create their own recipes, view all the recipes, edit and delete their recipes. The target audience for this app is anyone who is looking for low cholesterol food.
This website has a user-friendly interface with easy access to all information. This app has been developed so registered users can easily add, delete and edit there own recipes with there own personal database.


# User Stories

As a user, I want:

1. To view all recipe details which includes the name of the dish, meal, cooking time, servings, list of  ingredients and directions

2. To create my own account

3. To add new recipes


4. To edit and delete recipes on my account and all the recipes I've created

5. To view a list of my recipes on a separate page and see how many recipes I've created

6. to have the ability to use the site on all modern browsers

7. to use the site on tablet , mobile or pc.

8. I want to be able to add in notes to each dish so I can add my own thoughts, experiences or
things I want to remember about cooking the dish.

9. I want the site to be easy navigate


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

The Navbar is not fixed, when you enter the website are there 2 options , to login and register.
Once registered and logged in, there is a option to add a new recipe.
To view the recipes just click on the title Low Chloesterol food to view the recipes and within the recipe itself there is an option to edit and delete the recipe.On mobile, the links will display in a menu on the left hand side.

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
User stories testing:


1. To view all recipe details which includes the name of the dish, meal, 
   cooking time, servings, list of ingredients and directions.

- All recipes can be viewed without being logged in. You can view the dish, cooking time, servings, ingredients and directions within the modal. The first window will show the name and type of meal, then press open here to view the rest of the list.

2. To create my own account

- I created a few test accounts to test this functionality. Clicking on the "Register" button in the navbar opens the form, where I can input a username and password to create a new account. I tried registering as a user that already exits and the flash message comes up Username already exists.

3. To add new recipes

- I added plenty of test recipes to check the functionality and if I leave some of the required fields empty, I will not be able to submit the form. I can see the flash messages displayed if my input does not meet length requirement. 

4. To edit and delete recipes on my account and all the recipes I've created

- If I am the author a of selected recipe, I can see the buttons "Edit" and "Delete" in the recipe -  modals, and I can only delete and edit the recipes of said author.

5. To view a list of my recipes on a separate page and see how many recipes I've created

- All the recipes are shown when you click on the Low Chloesterol Recipe title, at the moment you would have to count the amount of recipes you have,  but a feature will be added in the future to count the amount of recipes.

6. to have the ability to use the site on all modern browsers

- I have checked the site on various browsers such as Chrome, Edge, Firefox and Opera.

7. to use the site on tablet , mobile or pc.

- I have checked the site on PC, Laptop, Tablet and Mobile and also used the Am I Responsive website.

8. I want to be able to add in notes to each dish so I can add my own thoughts, experiences or
things I want to remember about cooking the dish.

- Notes for this can be added in the directions.

9. I want the site to be easy navigate

-The site is easy to navigate with all links in the navbar. On mobile, the links on the left hand side under menu, and to view the recipes just click on the title Low Cholestrol Food.

### HTML validator
[W3C Markup Validator](https://validator.w3.org/)
All HTML pages passed , The only thing that failed was the jinja.

add_recipe:
<h2 align="center"><img src="test/add_recipe.png" width="400px"></h2>

edit_recipe:
<h2 align="center"><img src="test/edit_recipe.png" width="400px"></h2>

base:
<h2 align="center"><img src="test/base.png" width="400px"></h2>

login:
<h2 align="center"><img src="test/login.png" width="400px"></h2>

recipes:
<h2 align="center"><img src="test/recipes.png" width="400px"></h2>

register:
<h2 align="center"><img src="test/register.png" width="400px"></h2>

### CSS validator
[W3C Markup Validator](https://jigsaw.w3.org/css-validator/)
<h2 align="center"><img src="test/css.png" width="400px"></h2>

### PEP8 validator
[W3C Markup Validator](https://www.pythonchecker.com/)
<h2 align="center"><img src="test/pep8.png" width="400px"></h2>

The PEP8 vaildator failed on having no blank lines between the app.route() and the def function.
 
### Functionality/Unit Testing

On my previous attempt at this project, it failed on testing.
I have wrote a test which is in test.py, but I could not get it to connect to MongoDB.
I got in touch with tutor support who informed me that they won't be able to provide support for testing an application that uses mongodb, as it is not covered in the course materials.
I then emailed student support about this and they have confirmed that I don't need to worry about it.

# Compatibility and Responsiveness

This website had been being tested during the development across multiple browsers (Chrome, Safary, Opera, FireFox and Edge) and on multiple devices: mobile Samsung Galaxy, tablets and laptops and desktop PC.
As well as on Google Chrome's developer tools to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.
I also used Am I Responsive online tool for checking responsiveness on different devices.
Plenty of changes were made and necessary media queries added to make the website fully responsive.

# Bugs
I could not get postgres to work , I kept having the error:

psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory Is the server running locally and accepting connections on that socket?

Everything I tried did not work so I have decided to use MongoDB instead. I also had an error which was:

'Collection' object is not callable. If you meant to call the 'update' method on a 'Collection' object it is failing because no such method exists

This was related to the line mongo.db.starter.update({"_id": ObjectId(starter_id)}, edited_starter) in my edit_starters function in app.py, so I had downgrade pymongo from 4.3.3 to 3.12.3.

I also encountered a problem where after I have added my recipe, I then go to edit my recipe, but after I have edited my recipe the edit and delete buttons dissapear but I solved this by showing the username in the modal.

# Deployment

1. Set up environment variables.

- Create .env file in the root directory.
On the top of the file, add import os to set the environment variables in the operating system
Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax: 

- os.environ.setdefault("IP", "0.0.0.0")

- os.environ.setdefault("PORT", "5000") 

- os.environ.setdefault("SECRET_KEY", "secret_key")

- os.environ.setdefault("MONGO_URI", "")

- os.environ.setdefault("MONGO_DBNAME", "mongo-dbname")

2. Install all requirements from the requirements.txt file putting this command into your terminal:
pip3 freeze --local > requirements.txt

3. Create a Procfile, which is what Heroku looks for to know which file runs the app, and how to
run it by using the following command in the terminal:
echo web: python run.py > Procfile

4. git add, git commmit and git push files.

5. Log into Herouku and create a new app, assign a name and select a region.

6. From the Heroku dashboard link the new Heroku app to your GitHub repository:

 - Click on Deploy followed by Github.
 - Make sure your GitHub profile is displayed, then add your repository name then click 'Search'.
 - Once it finds your repo, click to connect to this app.

7. Click on the 'Settings' tab for your app, and then click on 'Reveal Config Vars', where
we can securely tell Heroku which variables are required. Set the following vars:
- IP : 0.0.0.0
- PORT : 5000
- SECRET_KEY : <your secret key>
- MONGO_URI : <link to your MongoDB database: myfirst cluster > connect > drivers>
- MONGO_DBNAME :  <link to your MongoDB database>


- These are the same that are in the env file.

8. Enable Automatic Deployment on the deploy tab.

9. The app will be deployed and ready to run. Click "Open App" to view the app.

# Credits

I would like to thank my my mentor , tutor and student support for there help.