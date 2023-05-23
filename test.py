import unittest
from flask import Flask, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_db'
mongo = PyMongo(app)

class EditRecipeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        recipe = {
            "name": "rice",
            "meal_type": "curry" ,
            "ingredients": "lihlih",
            "tools": "ff",
            "directions": "frggr",
            "cooking_time": "5665",
            "servings": "555",
            
        }
        x = mongo.db.recipes.insert_one(recipe)
        print(x)
    def tearDown(self):
        pass

    def test_edit_recipe(self):
        # Assuming the recipe_id exists in the database
        recipe_id = "646b90d25406a0604343fe04"  

        # Simulate a POST request with form data
        form_data = {
            "name": "New Recipe Name",
            "meal_type": "Lunch",
            "ingredients": "Ingredient 1, Ingredient 2",
            "tools": "Tool 1, Tool 2",
            "directions": "Step 1, Step 2",
            "cooking_time": "30 minutes",
            "servings": "2"
        }
        response = self.app.post(f"/edit_recipe/{recipe_id}", data=form_data)

        # Assert that the response has a successful status code (e.g., 200)
        self.assertEqual(response.status_code, 200)

        # Assert that the recipe in the database has been updated
        updated_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
        self.assertEqual(updated_recipe['name'], "New Recipe Name")
        self.assertEqual(updated_recipe['meal_type'], "Lunch")
        self.assertEqual(updated_recipe['ingredients'], "Ingredient 1, Ingredient 2")
        self.assertEqual(updated_recipe['tools'], "Tool 1, Tool 2")
        self.assertEqual(updated_recipe['directions'], "Step 1, Step 2")
        self.assertEqual(updated_recipe['cooking_time'], "30 minutes")
        self.assertEqual(updated_recipe['servings'], "2")


if __name__ == '__main__':
    unittest.main()