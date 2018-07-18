from flask_restplus import Resource


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