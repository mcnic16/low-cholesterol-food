

<h1 align="center">Low Cholesterol Recipes</h1>


[View live project]()


add screenshots here of full site on tablet, mobile and pc.




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


## Framework
Bootsrap


## Colour Scheme


## Typography


## Icons


## Wireframes


## Features


# Technologies Used


## Front-End


## Back-End


## Libraries


## Testing
validators , pep8 and python testing


# Compatibility and Responsiveness


# Bugs


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
MONGO_URI : 
MONGO_DBNAME :  <link to your MongoDB database>


These are the same that are in the env file.

8.Enable Automatic Deployment on the deploy tab.

9.The app will be deployed and ready to run. Click "Open App" to view the app.








# Credits
