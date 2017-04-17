from flask import render_template, request

from app import app
from app.models import ToDo


@app.route('/')
def index():
    todos = ToDo.objects.order_by('-time')
    return render_template('index.html', todos=todos)


@app.route('/add', methods=['post',])
def add():
    content = request.form.get('content')
    todo = ToDo(content=content)
    todo.save()
    
    todos = ToDo.objects.all()
    return render_template('index.html', todos=todos)


@app.route('/do/<string:todo_id>')
def do(todo_id):
    todo = ToDo.objects.get_or_404(id=todo_id)
    todo.status = 1
    todo.save()

    todos = ToDo.objects.all()
    return render_template("index.html", todos=todos)


@app.route('/undo/<string:todo_id>')
def undo(todo_id):
    todo = ToDo.objects.get_or_404(id=todo_id)
    todo.status = 0
    todo.save()
    
    todos = ToDo.objects.all()
    return render_template("index.html", todos=todos)


@app.route('/delete/<string:todo_id>')
def delete(todo_id):
    todo = ToDo.objects.get_or_404(id=todo_id)
    todo.delete()
    
    todos = ToDo.objects.all()
    return render_template("index.html", todos=todos)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
