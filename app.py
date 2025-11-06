from flask import Flask
from flask_restful import Api
from routes import InitRoutes
from os import environ
from app_data.definitions import server_port


app = Flask(__name__)
api = Api(app)

InitRoutes(api)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST','localhost')
    PORT = server_port
    app.run(HOST, PORT, debug=True)
    
    # http://localhost:5001/api/v1/hello
    # http://localhost:5001/api/v1/status?deviceId=2