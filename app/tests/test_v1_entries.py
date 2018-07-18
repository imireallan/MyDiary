import json
from app.tests.base import BaseTestCase



class TestEntry(BaseTestCase):
    """Test Entries Endpoints."""

    def create(self):
        return self.client.post(
            '/api/v1/entries', 
            data=json.dumps(self.data),
            content_type='application/json'
        )

    def test_create_entry(self):
        """Test create entry endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            self.assertIn(b"test1",res.data)


    def test_get_entries(self):
        """Test get entry endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            res = self.client.get(
                '/api/v1/entries',
                content_type='application/json'
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn(b"test",res.data )


    def test_get_one_entry(self):
        """Test get_one entry endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.get(
                '/api/v1/entries/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"test",result.data )

    def test_delete_entry(self):
        """Test delete entry endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.delete(
                '/api/v1/entries/{}'.format(res.get_json()['id'])
            )
            self.assertEqual(result.status_code, 204)
            self.assertNotIn(b'test', result.data)
            res = self.client.get(
                '/api/v1/entries/'
            )
            self.assertEqual(res.status_code, 404)

    def test_update_entry(self):
        """Test update entry endpoint
        """
        with self.client:
            res = self.create()
            self.assertEqual(res.status_code, 201)
            result = self.client.put(
                '/api/v1/entries/{}'.format(res.get_json()['id']),
                data=json.dumps({"title":"soccer", "contents":"france are the 2018 world champions"}),
                content_type='application/json'
            )
            self.assertEqual(result.status_code, 200)
            self.assertIn(b"soccer",result.data )