from flask import Flask
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='TestTODO API', description="A tutorial on flask-restplus")

ns = api.namespace('todos', description='TODO operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='Unique Id'),
    'task': fields.String(required=True, description='Task details')
})

class Task(object):

    def __init__(self):
        self.counter = 0
        self.todos = []

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        api.abort(404, f"Todo {id} doesn't exist")

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self,id):
        todo = self.get(id)
        self.todos.remove(todo)


TODO = Task()
TODO.create({"task":"Learn flask-restplus"})
TODO.create({"task":"??????"})
TODO.create({"task":"Profit!"})


@ns.route('/')
class TodoList(Resource):
    """Show all todo's, and POST new tasks"""
    @ns.doc('list_todos')
    @ns.marshal_list_with(todo)
    def get(self):
        """List all tasks."""
        return TODO.todos

    @ns.doc("delete_todo")
    @ns.response(204,'Todo Deleted')
    def delete(self, id):
        """Delete task given an id"""
        TODO.delete(id)
        return '', 204

    @ns.expect(todo)
    @ns.marshal_with(todo)
    def put(self,id):
        """Update a task given its id"""
        return TODO.update(id, api.payload)

if __name__ == "__main__":
    app.run(debug=True)