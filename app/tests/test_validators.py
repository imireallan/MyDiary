import unittest
import json
from app.tests.base import BaseTestCase
from app.tests.helpers import register_user, login_user

class TestValidatorsCase(BaseTestCase):
    "Class for testing validators"

    def test_username_is_required(self):
        """test username is a required field."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            username='',
            email='imireallan@gmail.com',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"username is a required field", res.data)

    def test_username_length(self):
        """test username requires at most 10 characters."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            username='imireallan1imireallan2',
            email='imireallan@gmail.com',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"username is too long", res.data)

    def test_email_length(self):
        """test email is a required field."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            username='imire',
            email='imireallanmoffatngiggelucaamugogokinyakinyanjui@gmail.com',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"email is too long", res.data)

    def test_email_is_required(self):
        """test email is a required field."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            username='imire',
            email='',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"email is a required field", res.data)

    def test_password_is_required(self):
        """test password is a required field."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password is a required field", res.data)

    def test_password_is_valid(self):
        """test password is not whitespace."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='      ',
            confirm='      '
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid password", res.data)

    def test_password_requires_6_characters(self):
        """test password requires atleast six characters."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='pass',
            confirm='pass'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password requires atlest 6 characters", res.data)

    def test_valid_email_format(self):
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallangmail.com',
            username='imire',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid email address", res.data)

    def test_password_must_match_to_register(self):
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='passwor',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"password mismatch", res.data)

    def test_non_digit_username(self):
        """test non-digit username."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='12345',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a non digit username", res.data)

    def test_valid_username(self):
        """test valid username format."""
        res = self.client.post(
        'api/v2/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='      ',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
        )
        self.assertTrue(res.status_code, 400)
        self.assertIn(b"Enter a valid username", res.data)

    def test_title_is_required(self):
        "Test title is a required property"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry_no_title
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"title is a required field", rv.data)

    def test_contents_is_required(self):
        "Test contents is a required property"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry_no_contents
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"contents is a required field", rv.data)

    def test_non_digit_contents(self):
        "test for non-digig contents."
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"title": "first test",
                    "contents": "11111111"
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter non digit contents", rv.data)

    def test_valid_contents(self):
        "test contents entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"title": "first test",
                    "contents": "    "
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter valid contents", rv.data)

    def test_valid_title(self):
        "test title entered in valid format"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"title": "    ",
                    "contents": "this is very awsome"
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"Enter a valid title", rv.data)

    def test_title_length(self):
        "test title is less than 50 characters"
        with self.client:
            res = register_user(self)
            self.assertTrue(res.status_code, 201)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create entry by making a POST request
            rv = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=json.dumps(
                    {"title": "thisisthelongesttitleeveranitshouldbemorethanfiftycharacterslong",
                    "contents": "this is very awsome"
                    })
                )
            self.assertEqual(rv.status_code, 400)
            self.assertIn(b"title is too long", rv.data)
