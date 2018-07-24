import unittest
import datetime


from app.tests.base import BaseTestCase
from app.apis.models.model import User


class TestUserModel(BaseTestCase):

    def test_generate_token(self):
        token = self.user.generate_token(self.user.id)
        self.assertTrue(isinstance(token, str))

    def test_decode_auth_token(self):
        
        token = self.user.generate_token(self.user.id)
        self.assertTrue(isinstance(token, str))
        self.assertTrue(User.decode_token(token) == 1)


if __name__ == '__main__':
    unittest.main()