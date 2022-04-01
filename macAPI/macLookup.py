from flask import Flask
from flask_restful import Resource, Api, request
import json

app = Flask(__name__)
api = Api(app)

class MACs(Resource):
    def get(self):
        args = request.args # load in args
        lookup = args['lookup'] # set variable based on arg
        f = open('mac-vendors-export.json') # Opening json file
        data = json.load(f) #Load into json object
        try: # search list of json dicts against mac address arg
            search = next(item for item in data if item['macPrefix'] == lookup) 
        except StopIteration: #catch the exception if MAC not present
            search = 'Not Present'
        return {'search': search}, 200  # return data and 200 OK code
        f.close() #close file

api.add_resource(MACs, '/MACs')  # '/MACs' is our entry point

if __name__ == '__main__':
    app.run()  # run our Flask app