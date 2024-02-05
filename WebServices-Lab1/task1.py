from flask import Flask
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
# make the class
class GetProduct(Resource):
    def get(self):

        
        # the file to be converted to 
        # json format
        filename = 'WebServices-Lab1/product.txt'
        
        # dictionary where the lines from
        # text will be stored
        dict1 = {}
        
        # creating dictionary
        with open(filename) as fh:
        
            for line in fh:
        
                # reads each line and trims of extra the spaces 
                # and gives only the valid words
                command, description = line.strip().split(None, 1)
        
                dict1[command] = description.strip()
        
        # creating json file
        # the JSON file is named as test1
        out_file = open("WebServices-Lab1/output.json", "w")
        json.dump(dict1, out_file, indent = 4, sort_keys = False)
        out_file.close()


        # read the file back in and 
        # send it through the API
        f = open('WebServices-Lab1/output.json')
        data = json.load(f)

        return data
            

        

                
        
     
      



# register the URL
api.add_resource(GetProduct, '/getProduct')



if __name__ == '__main__':
    app.run(debug=True)