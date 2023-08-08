from flask import Flask , request
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"Hello":"world"}
    
api.add_resource(HelloWorld,"/") #api endpoint from that we will get request to this

todos={}

class TodoSimple(Resource):
    def get(self, todo_id): # we will getting todo_id from the get request 
        return {todo_id: todos[todo_id]} # adding todo id into todolist 
    
    def put(self,todo_id):
        todos[todo_id]=request.form['data'] # it will take data thaat will given as a body in the put method 
        return {todo_id : todos[todo_id]}

api.add_resource(TodoSimple,'/<string:todo_id>')

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo1,"/Todo1")
api.add_resource(Todo2,"/Todo2")
api.add_resource(Todo3,"/Todo3")

if __name__=='__main__':
    app.run(debug=True)