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
        id = 0
        if len(self.no_of_entries) == 0:
            id = 1
        else:
            id = self.no_of_entries[-1]["id"] +1
        data["id"] = id
        data["creation_date"] = str(datetime.now().strftime('%d-%b-%Y : %H:%M:%S'))
        data["title"] = data["title"].strip()
        data["contents"] = data["contents"].strip()
        if data["title"] == "":
            api.abort(400, "'title' is a required field.")
        elif data["contents"] == "":
            api.abort(400, "'title' is a required field.")
        self.no_of_entries.append(data)
        return data

    def get_one(self, entry_id):
        """Method for fetching one entry by its id"""
        entry = [entry for entry in self.no_of_entries if entry["id"] == entry_id]

        if not entry:
            api.abort(404, "Entry {} does not exist".format(entry_id))
        return entry

    def delete_entry(self, entry_id):
        "Method for deleting an entry"

        entry = self.get_one(entry_id)
        self.no_of_entries.remove(entry[0])

    def update_entry(self, entry_id, data):
        """Method for updating an entry"""

        entry = self.get_one(entry_id)
        data['modified_date'] = str(datetime.now().strftime('%d-%b-%Y : %H:%M:%S'))
        entry[0].update(data)
        return entry

    def get_all(self):
        """Method for returning all entries."""
        entries = [entries for entries in self.no_of_entries]
        if not entries:
            api.abort(404, "No Entries Found.")
        return entries
