from flask import Flask
from flask_restful import Api, Resource, reqparse
from mongo_c import init_mongo, mongo
from user_m import User
from bson.objectid import ObjectId

app = Flask(__name__)
init_mongo(app)

api = Api(app)

class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        user = User(**args)
        result = mongo.db.users.insert_one(user.to_dict())
        return {'id': str(result.inserted_id)}, 201

    def get(self):
        users = mongo.db.users.find()
        result = []
        for user in users:
            user["_id"] = str(user["_id"])
            result.append(user)
        return result

class UserByIdResource(Resource):
    def get(self, id):
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if user:
            user["_id"] = str(user["_id"])
            return user
        else:
            return {'error': 'User not found'}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('password', required=True)
        args = parser.parse_args()
        user = User(**args)
        result = mongo.db.users.update_one({"_id": ObjectId(id)}, {"set": user.to_dict()})
        if result.matched_count:
            return {'successfully Updated': True}
        else:
            return {'error': 'User not found'}, 404

    def delete(self, id):
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {'successfully Deleted': True}
        else:
            return {'error': 'User not found'}, 404

api.add_resource(UserResource, '/users')
api.add_resource(UserByIdResource, '/users/<string:id>')

if __name__ == "__main__":
    app.run(debug=True, port=5009)
