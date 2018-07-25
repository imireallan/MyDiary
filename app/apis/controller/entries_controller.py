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
    @api.header('Authorization', type=str, description='access token')
    def post(user_id, self):
        """Creates a new Entry."""
        args = entry_parser.parse_args()

        if args["title"] and args["contents"]:
            title = args["title"]
            contents = args["contents"]
            Entry.add_entry(cursor, title, contents, user_id)
            return {"message": "Entry added successfully"}
        return {"Warning": "'title' and 'contents' are required fields"}, 400