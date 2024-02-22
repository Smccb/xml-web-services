from flask import Flask
from flask_restful import Resource, Api
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads
from bson.objectid import ObjectId

app = Flask(__name__)
api = Api(app)


#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}
#api.add_resource(HelloWorld, '/')


# make the class
class GetAll(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data

        results = dumps(collection.find())
        return json.loads(results)
    
api.add_resource(GetAll, '/getAll')


# make the class
class GetOne(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data
        # ID of the object
        id = '65c372ad7d8fee19b55a8aa2'
        query = {"_id": ObjectId(id)}
        filter = {"_id": 0}
        # find it
        results = collection.find_one(query, filter)
        print(results)
        # dump to JSON
        results = dumps(results)
        #return
        return json.loads(results)
    

api.add_resource(GetOne, '/getOne')


from flask_restful import reqparse
class HelloWorld(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        res = parser.add_argument('username', type=str, location='args')
        args = parser.parse_args()
        name = args['username']
        print(name)
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/')




# make the class
#modified, Task C
class InsertOne(Resource):
    def get(self):
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data

        #parser = reqparse.RequestParser()
        #res = parser.add_argument('saleId', type=str, location='args')
        #res = parser.add_argument('orderId', type=str, location='args')
        #res = parser.add_argument('productId', type=str, location='args')
        #res = parser.add_argument('quantity', type=str, location='args')
        #args = parser.parse_args()

        #saleId = args['saleId']
        #orderId = args['orderId']
        #productId = args['productId']
        #quitity = args['quantity']

        #print(saleId)


        # Record to be inserted
        #newRecord= {"SaleId": saleId, "OrderId": orderId, "ProductId": productId, "Quantity": quitity}
        newRecord= {"SaleId": 1, "OrderId": 1, "ProductId": 3, "Quantity": 3}

        # find it
        res = collection.insert_one(newRecord)
        #return
        return {"status":"inserted"}
api.add_resource(InsertOne, '/insertOne')


#tasks
#Task A
class individualRecordsRequest(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        res = parser.add_argument('id', type=str, location='args')
        args = parser.parse_args()
        id = args['id']
        print(id)
        
        client = MongoClient("mongodb://root:example@localhost:27017/")
        db = client.sales
        collection = db.sales_data
        
        query = {"_id": ObjectId(id)}
        filter = {"_id": 0}
        # find it
        results = collection.find_one(query, filter)
        print(results)
        # dump to JSON
        results = dumps(results)
        #return
        return json.loads(results)
        
api.add_resource(individualRecordsRequest, '/getSingleById')


if __name__ == '__main__':
    app.run(debug=True)