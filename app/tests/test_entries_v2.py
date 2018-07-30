import unittest
from app.tests.base import BaseTestCase
from app.tests.helpers import register_user, login_user


class EntriesTestCase(BaseTestCase):
    """Represents the entries test case"""

    def test_entry_creation(self):
        """Test API can create a entry."""
    
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
                data=self.entry
                )
            self.assertEqual(rv.status_code, 201)
            self.assertIn(b'Entry added successfully', rv.data)

    def test_api_can_get_all_entries(self):
        """Test API can get all."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry
                )
            self.assertEqual(res.status_code, 201)

            # get all the entries that belong to a specific user
            res = self.client.get(
                'api/v2/entries',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first test', res.data)

    def test_api_can_get_entry_by_id(self):
        """Test API can get a single entry by using it's id."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry
                )
            self.assertEqual(res.status_code, 201)

            # get all the entries that belong to a specific user
            res = self.client.get(
                'api/v2/entries/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b'first test', res.data)

    def test_entry_can_be_edited(self):
        """Test API can edit an existing entry. (PUT request)"""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry
                )
            self.assertEqual(res.status_code, 201)
            
            # modify an entry
            rv = self.client.put(
                '/api/v2/entries/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.update_entry
                )
            self.assertEqual(rv.status_code, 200)

            res = self.client.get(
                'api/v2/entries/1',
                 headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
            )
            self.assertIn(b'first edition', res.data)

    def test_entry_deletion(self):
        """Test API can delete an existing entry."""
        with self.client:
            register_user(self)
            res = login_user(self)
            access_token = res.get_json()['token']

            # create an entry
            res = self.client.post(
                'api/v2/entries',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                },
                data=self.entry
                )
            self.assertEqual(res.status_code, 201)
            
            # delete an entry
            res = self.client.delete(
                '/api/v2/entries/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertTrue(res.status_code, 200)
            self.assertIn(b"Entry deleted successully", res.data)
            # test for entry not found
            res = self.client.get(
                '/api/v2/entries/1',
                headers={
                    "x-access-token": access_token,
                    "content-type": "application/json"
                }
                )
            self.assertEqual(res.status_code, 404)
            self.assertIn(b"Entry 1 not found", res.data)

if __name__ == "__main__":
    unittest.main()