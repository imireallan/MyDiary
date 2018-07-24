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

class EntriesTestCase(BaseTestCase):
    """Represents the entries test case"""

    def test_entry_creation(self):
        """Test API can create a entry."""
        with self.client:
            register_user(self)
            res = login_user(self)
            token = res.get_json()['access_token']

            # create entry by making a POST request
            res = self.client.post(
                'api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
                data=self.entry)
            self.assertEqual(res.status_code, 201)
            self.assertIn(b'first title', res.data)

    def test_api_can_get_all_entries(self):
        """Test API can get all."""
        with self.client:
            register_user(self)
            res = login_user(self)
            token = res.get_json()['access_token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
                data=self.entry)
            self.assertEqual(res.status_code, 201)

            # get all the entries that belong to a specific user
            res = self.client.get(
                'api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first title', res.data)

    def test_api_can_get_entry_by_id(self):
        """Test API can get a single entry by using it's id."""
        with self.client:
            register_user(self)
            res = login_user(self)
            token = res.get_json()['access_token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
                data=self.entry)
            self.assertEqual(res.status_code, 201)

            results = res.get_json()
            result = self.client().get(
                '/api/v2/entries/{}'.format(results['id']),
                headers=dict(Authorization="Bearer " + access_token))
           
            self.assertEqual(result.status_code, 200)
            self.assertIn(b'first title', res.data)

    def test_entry_can_be_edited(self):
        """Test API can edit an existing entry. (PUT request)"""
        with self.client:
            register_user(self)
            res = login_user(self)
            token = res.get_json()['access_token']

            # create an entry
            res = self.client.post(
                '/api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
                data=self.entry)
            self.assertEqual(res.status_code, 201)

            results = res.get_json()

            rv = self.client().put(
                '/api/v2/entries/{}'.format(results['id']),
                headers=dict(Authorization="Bearer " + token),
                data={
                    "title": "world cup", "contents": "France are the champions"
                })
            self.assertEqual(rv.status_code, 200)

            results = self.client().get(
                '/api/v2/entries/{}'.format(results['id']),
                headers=dict(Authorization="Bearer " + token))
            self.assertIn(b'world cup', results.data)

    def test_entry_deletion(self):
        """Test API can delete an existing entry."""
        with self.client:
            register_user(self)
            res = login_user(self)
            token = res.get_json()['access_token']

            # create an entry
            res = self.client.post(
                '/api/v2/entries',
                headers=dict(Authorization="Bearer " + token),
                data=self.entry)
            self.assertEqual(res.status_code, 201)

            results = res.get_json()

            res = self.client().delete(
                '/api/v2/entries/{}'.format(results['id']),
                headers=dict(Authorization="Bearer " + token),)
            self.assertEqual(res.status_code, 204)

            result = self.client().get(
                '/api/v2/entries/1',
                headers=dict(Authorization="Bearer " + token))
            self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    unittest.main()