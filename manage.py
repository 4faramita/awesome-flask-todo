# -*- coding: utf-8 -*-

from flask_script import Manager, Server

from app import app
from app.models import ToDo

manager = Manager(app)

@manager.command
def save_todo():
    todo = ToDo(content='My first todo!')
    todo.save()

manager.add_command(
    'runserver',
    Server(host='127.0.0.1', port=5000, use_debugger=True))

if __name__ == '__main__':
    manager.run()
