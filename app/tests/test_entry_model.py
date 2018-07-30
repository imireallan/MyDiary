import unittest

from app.tests.base import BaseTestCase
from app.apis.models.model import Entry, User


class TestEntryModel(BaseTestCase):

    def test_get_entry_by_id(self):
        User.create_user(self.cursor, "imireallan", "imire@gmail.com", "password")
        data = Entry.add_entry(self.cursor, "first entry model test", "testing is very essential", 1)
        result = Entry.get_entry_by_id(self.dict_cursor, 1)
        self.assertIn("first entry model test", result.values())

    def test_get_all_entries(self):
        User.create_user(self.cursor, "imireallan", "imire@gmail.com", "password")
        data = Entry.add_entry(self.cursor, "first entry model test", "testing is very essential", 1)
        result = Entry.get_all(self.dict_cursor, 1)
        self.assertIn("first entry model test", result[0].values())


if __name__ == '__main__':
    unittest.main()