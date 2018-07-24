import unittest
import json
from app.tests.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/auth/signup',
        data=json.dumps(dict(
            email='imireallan@gmail.com',
            username='imire',
            password='password',
            confirm='password'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            username='imireallan@gmail.com',
            password='password'
        )),
        content_type='application/json'
    )


class AuthTestCase(BaseTestCase):

    def test_login_for_registered_user(self):
            """ Test for login of registered-user login """
            with self.client:
                # signup
                res = register_user(self)
                self.assertEqual(res.status_code, 201)

                # login
                res = login_user(self)
                data = res.get_json()
                self.assertTrue(data['Authorization'])
                self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
