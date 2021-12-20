from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HealthCheck(Resource):
    def get(self):
        return {"healthy": 200}, 200


class Ping(Resource):
    def get(self):
        return {"pong": 200}, 200

api.add_resource(HealthCheck, '/health')
api.add_resource(Ping, '/ping')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80, debug=True)

#Elliott Arnold  12-19-21 7-11