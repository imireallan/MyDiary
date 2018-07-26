import unittest
import datetime


from app.tests.base import BaseTestCase
from app.apis.models.model import User


class TestUserModel(BaseTestCase):

    def test_generate_token(self):
        token = User.generate_token(self.user.id)
        self.assertTrue(isinstance(token, str))

    def test_get_user_by_username(self):
        data = User.create_user(self.cursor, "imireallan", "imire@gmail.com", "password")
        user = User.get_user_by_username(self.dict_cursor, "imireallan")
        self.assertIn('imireallan', user.values())


if __name__ == '__main__':
    unittest.main()