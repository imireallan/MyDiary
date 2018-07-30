# third-party imports
from flask_restplus import Resource

# local imports
from ..utils.entries_model import api, entries, post_entries, entry_parser, update_entry_parser
from ..utils.decorators import token_required
from ..utils.validators import validate_entry_data
from ..models.model import Entry
from app.database import Database


conn = Database()
cursor = conn.cursor
dict_cursor = conn.dict_cursor

@api.route("/entries")
class EntryList(Resource):
    """Displays a list of all entries and lets you POST to add new entries."""

    @api.expect(post_entries)
    @api.doc('adds an entry')
    @api.response(201, "Created")
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def post(user_id, self):
        """Creates a new Entry."""
        args = entry_parser.parse_args()

        # validate the entry payload
        invalid_data = validate_entry_data(args)
        if invalid_data:
            return invalid_data

        title = args["title"]
        contents = args["contents"]
        Entry.add_entry(cursor, title, contents, user_id)
        return {"message": "Entry added successfully"}, 201

    @api.doc("list_entries")
    @api.response(404, "Entries Not Found")
    @api.marshal_list_with(entries, envelope="entries")
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def get(user_id, self):
        """List all Entries"""
        entries = Entry.get_all(dict_cursor, user_id)
        if not entries:
            api.abort(404, "No entries for user {}".format(user_id))
        return entries

@api.route("/entries/<int:entryId>")
@api.param("entryId", "entry identifier")
@api.response(404, 'Entry not found')
class EntryClass(Resource):
    """Displays a single entry item and lets you delete them."""

    @api.marshal_with(entries)
    @api.doc('get one entry')
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def get(user_id, self, entryId):
        """Displays a single Entry."""
        entry = Entry.get_entry_by_id(dict_cursor, entryId)
        if entry["user_id"] != str(user_id):
            api.abort(401, "Unauthorized to view this entry")
        return entry


    @api.doc('updates an entry')
    @api.expect(post_entries)
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def put(user_id, self, entryId):
        """Updates a single Entry."""
        args = update_entry_parser.parse_args()
        Entry.modify_entry(dict_cursor, cursor, args["title"], args["contents"], entryId, user_id)
        return {"message": "Updated successfully"}

    @api.doc('deletes an entry')
    @api.response(204, 'Entry Deleted')
    @token_required
    @api.doc(security='apikey')
    @api.header('x-access-token', type=str, description='access token')
    def delete(user_id, self, entryId):
        """Deletes a single Entry."""

        Entry.delete_entry(dict_cursor, cursor, entryId, user_id)
        return {"message": "Entry deleted successully"}, 200