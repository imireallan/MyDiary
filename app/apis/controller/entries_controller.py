# third-party imports
from flask_restplus import Resource

# local imports
from ..utils.entries_model import api, entries, post_entries, entry_parser, update_entry_parser
from ..utils.decorators import token_required
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

        if args["title"] and args["contents"]:
            title = args["title"]
            contents = args["contents"]
            Entry.add_entry(cursor, title, contents, user_id)
            return {"message": "Entry added successfully"}
        return {"Warning": "'title' and 'contents' are required fields"}, 400

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
    def get(user_id, self, entryId):
        # import pdb;pdb.set_trace()
        """Displays a single Entry."""
        data = Entry.get_entry(dict_cursor, user_id, entryId)
        entry = {key:value for key, value in data.items()}
        print(entry)
        if not entry:
            api.abort(404, "Entry {} not found".format(entryId))
        return entry
        