# third-party imports
from flask_restplus import Resource

# local imports
from ..models.entries import Entry as EntryClass
from ..utils.dto import EntriesDto

api = EntriesDto.api
entries = EntriesDto.entries

entry = EntryClass()

@api.route("/entries")
class EntryList(Resource):
    """Displays a list of all entries and lets you POST to add new entries."""

    @api.expect(entries)
    @api.doc('creates an entry')
    @api.response(201, "Created")
    @api.marshal_with(entries)
    def post(self):
        """Creates a new Entry."""
        return entry.create_entry(api.payload),201

    @api.doc("list_entries")
    @api.response(404, "Entries Not Found")
    @api.marshal_list_with(entries, envelope="entries")
    def get(self):
        """List all Entries"""
        entries = entry.no_of_entries
        if not entries:
            api.abort(404)
        else:
            return entries

@api.route("/entries/<int:entryId>")
@api.param("entryId", "entry identifier")
@api.response(404, 'Entry not found')
class Entry(Resource):
    """Displays a single entry item and lets you delete them."""

    @api.marshal_with(entries)
    @api.doc('get one entry')
    def get(self, entryId):
        """Displays a single Entry."""
        return entry.get_one(entryId)

    @api.marshal_with(entries)
    @api.doc('updates an entry')
    @api.expect(entries)
    def put(self, entryId):
        """Updates a single Entry."""
        return entry.update_entry(entryId, api.payload)

    @api.marshal_with(entries)
    @api.doc('deletes an entry')
    @api.response(204, 'Entry Deleted')
    def delete(self, entryId):
        """Deletes a single Entry."""
        entry.delete_entry(entryId)
        return '',204
