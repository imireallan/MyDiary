from flask_restplus import Resource


from ..models.entries import Entry as EntryClass
from ..utils.dto import EntriesDto 



api = EntriesDto.api
entries = EntriesDto.entries


entry = EntryClass()