#!/usr/bin/env python
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
    if username == 'admin':
        return 'admin' # tsk tsk
    return None

@auth.error_handler
def unathorised():
    return make_response(jsonify({"error": "Unauthorised Access"}), 403)

tasks = [
     {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/todo/api/v1/tasks", methods=["GET"])
@auth.login_required
def get_tasks():
    """
    Return all tasks in the database.
    """
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    """
    Return the json response for a task when provided its `id`

    Return 404 if out of range
    """
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
@app.errorhandler(400)
def not_found(error):
    """
    Create a response that is suitable for json. Does not result in ugly 404 W3 html response. We should always try return sanitized or obsfucated data about our platform but in a manner that still provides details to the user.
    """
    return make_response(jsonify({'error':'Not Found'}), 404)

@app.route('/todo/api/v1/tasks', methods=["POST"])
@auth.login_required
def create_task():
    """
    Send a POST request to update the tasks list. Abort with 400 status if does not contain 'title'.

    Success returns a 201
    """
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task':task}, 201)

@app.route("/todo/api/v1/tasks/<int:task_id>", methods=["PUT"])
@auth.login_required
def update_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description']
    )
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})
    
@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['DELETE'])
@auth.login_required
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result':True})

@app.route("/")
def index():
    return "Home Page"

if __name__ == "__main__":
    app.run(debug=True)