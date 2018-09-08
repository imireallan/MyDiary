from flask_restplus import Namespace, fields, reqparse

api = Namespace("entries", description="Entries related operations")

entries = api.model(
    "entries", {
    "id": fields.Integer(readonly=True),
    "title":fields.String(required=True, description="The entry title"),
    "contents":fields.String(required=True, description="The entry contents"),
    "user_id":fields.String(required=True, description="The entry user_id"),
    "created_at":fields.String(required=True, description="The entry creation date")
    })

post_entries = api.model(
    "post_entries",{
        "title": fields.String(required=True,description="entries title", example='This is my first entry.'),
        "contents": fields.String(required=True,description="entries contents", example='This is my first content.')
    }
)

entry_parser = reqparse.RequestParser()
entry_parser.add_argument('title', required=True, type=str, help='title should be a string')
entry_parser.add_argument('contents', required=True, type=str, help='contents should be a string')

update_entry_parser = reqparse.RequestParser()
update_entry_parser.add_argument('title', required=True, type=str, help='title should be a string')
update_entry_parser.add_argument('contents', required=True, type=str, help='contents should be a string')