from flask_restplus import Namespace, fields

class EntriesDto(object):
    api = Namespace("entries", description="Entries related operations")
    entries = api.model(
        "entries", {
        "id": fields.Integer(readonly=True),
        "title":fields.String(required=True, description="The entry title"),
        "contents":fields.String(required=True, description="The entry contents")
        }
    )
