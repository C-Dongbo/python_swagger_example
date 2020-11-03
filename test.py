import json
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
import requests


app = Flask(__name__)
api = Api(app, version='1.0', title='Swagger-test')
ns = api.namespace('Swagger-test')


hello_world_api_model = api.model('test', {
    'input': fields.String(required=True, example='hello world')
})




@ns.route('/hello_world')
class Example(Resource):
    @api.expect(hello_world_api_model)
    def post(self):
        result = request.json['input']
        return jsonify({"result" : result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2222, threaded=True)

