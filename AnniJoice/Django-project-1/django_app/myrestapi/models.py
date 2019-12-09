from mongoengine import Document, EmbeddedDocument, fields

class Tool(Document):
   name = fields.StringField(required=True)
   votes = fields.IntField(required=True)
