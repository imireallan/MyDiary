"""Contains data structures that store data in memory."""

from datetime import datetime

class Entry(object):
    """Data structure for the entries."""
    def __init__(self):
        self.entries = []

    def create_entry(self, data):
        """"Adds an Entry"""
        data['id'] = int(len(self.entries) + 1)
        data['title'] = data['title'].strip()
        data['contents'] = data['contents'].strip()
        data['date_created'] = datetime.utcnow()
        data['date_modified'] = datetime.utcnow()
        self.entries.append(data)
