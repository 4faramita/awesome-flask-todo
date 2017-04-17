import datetime
import unittest

from  flask_mongoengine.wtf import model_form

from app import db, app


class ToDo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

ToDoForm = model_form(ToDo)


class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        '''Clear data from each test'''
        todos = Todo.objects.all()
        for todo in todos:
            todo.delete()


    def test_index(self):
        rv = self.app.get('/')
        assert 'To-Do List' in rv.data


    def test_empty(self):
        rv = self.app.get('/')
        assert "No todos, please add" in rv.data


    def test_add(self):
        self.app.post('/add', data=dict(content='test add todo'))
        todo = ToDo.objects.get_or_404(content='test add todo')
        assert todo is not None


    def test_none(self):
        try:
            todo = ToDo.objects.get_or_404(content='test none')
        except HTTPException as e:
            assert e.code == 404


    def test_done(self):
        todo = ToDo(content='done todo')
        todo.save()
        url = '/do/' + str(todo.id)
        rv = self.app.get(url)
        assert '/undone/' + str(todo.id) in rv.data

    '''
    def test_undone_todo(self):
        todo = Todo(content='test undone todo')
        todo.save()
        url = '/undone/' + str(todo.id)
        rv = self.app.get(url)
        assert '/done/' + str(todo.id) in rv.data


    def test_delete_todo(self):
        todo = Todo(content='test delete done')
        todo.save()
        url = '/delete/' + str(todo.id)
        rv = self.app.get(url)
        assert "No todos, please add" in rv.data


    def test_404(self):
        rv = self.app.get('/404test')
        assert "Not Found" in rv.data
    '''