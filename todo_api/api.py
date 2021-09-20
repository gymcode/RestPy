from flask import Flask; 
from flask_restful import Resource, Api

# initializing the app 
app = Flask(__name__)

#  initialize the apis
api = Api(app)

class HelloWorld (Resource):
    def get(self): 
        return {"data": "hello, Kenneth"}

# creating end points 
api.add_resource(HelloWorld, "/helloworld")
# api.add_resource(HelloName, "/helloname/<string:name>")

if __name__ == "__main__": 
    app.run(debug=True)