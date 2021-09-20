from flask import Flask; 
from flask_restful import Resource, Api

# initializing the app 
app = Flask(__name__)

#  initialize the apis
api = Api(app)


if __name__ == "__main__": 
    app.run(debug=True)