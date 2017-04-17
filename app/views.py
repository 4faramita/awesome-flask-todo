from flask import render_template

from app import app
from app.models import ToDo


@app.route('/')
def index():
    todos = ToDo.objects.all()
    return render_template('index.html', todos=todos)
