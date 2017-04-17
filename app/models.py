import datetime

from  flask_mongoengine.wtf import model_form

from app import db


class ToDo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

ToDoForm = model_form(ToDo)
