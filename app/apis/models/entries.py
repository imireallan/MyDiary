from datetime import datetime

from ..utils.dto import EntriesDto

api = EntriesDto.api

class Entry(object):
    """ CLASS FOR ADDING, EDITING AND DELETING DIARY ENTRIES."""

    def __init__(self):
        """constructor method"""

        self.no_of_entries = []

    def create_entry(self, data):
        """Method for creating an entry"""

        data["id"] = int(len(self.no_of_entries) + 1)
        self.no_of_entries.append(data)
        return data

    def get_one(self, id):
        """Method for fetching one entry by its id"""
        entry = [entry for entry in self.no_of_entries if entry["id"] == id]

        if not entry:
            api.abort(404, "Entry {} does not exist".format(id))
        
        return entry

    def delete_entry(self, id):
        "Method for deleting an entry"

        entry = self.get_one(id)
        self.no_of_entries.remove(entry[0])

    def update_entry(self, id, data):
        """Method for updating an entry"""

        entry = self.get_one(id)
        entry[0].update(data)
        return entry
