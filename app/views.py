from flask import render_template, request

from app import app
from app.models import ToDo


@app.route('/')
def index():
    todos = ToDo.objects.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['post',])
def add():
    content = request.form.get('content')
    todo = ToDo(content=content)
    todo.save()
    
    todos = ToDo.objects.all()
    return render_template('index.html', todos=todos)
