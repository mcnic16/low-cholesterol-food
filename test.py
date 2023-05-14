import unittest
from flask import url_for
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask

app = Flask(__name__)


class TestRegistration(unittest.TestCase):

    def setUp(self):
        # create test Flask app
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_register_success(self):
        # test successful registration
        with self.app as c:
            # simulate POST request with form data
            form_data = ImmutableMultiDict([
                ('username', 'testuser'),
                ('password', 'testpassword'),
                ('confirm_password', 'testpassword')
            ])
            response = c.post('/register', data=form_data, follow_redirects=True)

            # check that the user was redirected to the profile page
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Registration Successful!", response.data)

    def test_register_username_exists(self):
        # test registration with existing username
        with self.app as c:
            # simulate POST request with form data
            form_data = ImmutableMultiDict([
                ('username', 'existinguser'),
                ('password', 'testpassword'),
                ('confirm_password', 'testpassword')
            ])
            response = c.post('/register', data=form_data, follow_redirects=True)

            # check that the user was redirected back to the registration page
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Username already exists", response.data)

if __name__ == '__main__':
    unittest.main()