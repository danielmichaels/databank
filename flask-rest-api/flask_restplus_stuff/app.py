from flask import Flask, request
from flask_restplus import Api, Resource, fields
from datetime import datetime


app = Flask(__name__)
api = Api(app)

todos = {}

model = api.model('Model', {
    'name': fields.String,
    'address': fields.String,
    'date_updated': fields.DateTime(dt_format='rfc_822')
})

class TodoDao(object):
    def __init__(self, name, address, dtg):
        self.name = name
        self.address = address
        self.dtg = dtg

@api.route('/todo')
class Todo(Resource):
    @api.marshal_with(model, envelope='resource')
    def get(self, **kwargs):
        return {
            TodoDao(name='bob', address='123 fake st',
            dtg=datetime.now)
        }

if __name__ == "__main__":
    app.run(debug=True)
