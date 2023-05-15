import unittest
from flask import Flask, session, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
mongo = PyMongo(app)
app.secret_key = 'your_secret_key'


class TestProfile(unittest.TestCase):
    
    def setUp(self):
        # Create test Flask app
        app.testing = True
        self.app = app.test_client()
        
    def tearDown(self):
        pass
    
    def test_profile_get(self):
        # Simulate GET request to profile with a username
        with self.app as c:
            # Set the session user to simulate an authenticated user
            with c.session_transaction() as session:
                session['user'] = 'testuser'
            
            response = c.get('/profile/testuser')
            
            # Check that the response status code is 200 (OK)
            self.assertEqual(response.status_code, 200)
            
            # Check that the rendered template contains the correct username
            expected_html = render_template("profile.html", username="testuser")
            self.assertEqual(response.get_data(as_text=True), expected_html)
    
    def test_profile_post(self):
        # Simulate POST request to profile with a username
        with self.app as c:
            # Set the session user to simulate an authenticated user
            with c.session_transaction() as session:
                session['user'] = 'testuser'
            
            response = c.post('/profile/testuser')
            
            # Check that the response status code is 200 (OK)
            self.assertEqual(response.status_code, 200)
            
            # Check that the rendered template contains the correct username
            expected_html = render_template("profile.html", username="testuser")
            self.assertEqual(response.get_data(as_text=True), expected_html)


if __name__ == '__main__':
    unittest.main()