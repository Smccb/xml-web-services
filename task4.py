#exmaple 1
import graphene
class Patron(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    age = graphene.Int()


class Query(graphene.ObjectType):
    patron = graphene.Field(Patron)
    def resolve_patron(root, info):
        return Patron(id=1, name="Syrus", age=27)
    

schema = graphene.Schema(query=Query)
query = """
    query something{
    patron {
        id
        name
        age
}
}
"""

result = schema.execute(query)
print(result)
print(result.data["patron"])


#example 2
import graphene
# Define the schema
class Product(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    cost = graphene.Decimal()


# Mapping values to Products
class Query(graphene.ObjectType):
    product = graphene.Field(Product)
    def resolve_product1(root, info):
        return Product(id=1, title="Apple", cost="2.0")
    product2 = graphene.Field(Product)
    def resolve_product2(root, info):
        return Product(id=2, title="Ham", cost="1.0")
    product3 = graphene.Field(Product)
    def resolve_product3(root, info):
        return Product(id=3, title="Juice", cost="4.2")
    

#
# Running a query on the data
#
schema = graphene.Schema(query=Query)
query = """
{
    product3 {
        id
        title
    }
}
"""
result = schema.execute(query)
print(result)


#example 3
from flask import Flask
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)
class GetProducts(Resource):
    def get(self):
        return {'id': '1221'}
    
api.add_resource(GetProducts, '/getProducts')
if __name__ == '__main__':
    app.run(debug=True)


import graphene
import requests
import json
# Define the schema
class Product(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    cost = graphene.Decimal()


# Mapping values to Products
class Query(graphene.ObjectType):
    product = graphene.Field(Product)
    def resolve_product(root, info):
        data = requests.get('http://127.0.0.1:5000/getProducts')
        print(data.text)
        '''
        This is a sample fo what the API will return.
        {
            "id": "1221"
        }
        '''
        # parse the JSON
        json_content = json.loads(data.text)

        print(json_content)
        # Extract the ID from the JSON
        extractedId = json_content['id']
        print(extractedId)
        # Send back the ID in a Product
        return Product(id=extractedId)
    

#
# Running a query on the data
#
schema = graphene.Schema(query=Query)
query = """
    {
        product {
            id
            title
        }
    }
"""

result = schema.execute(query)
print(result)
