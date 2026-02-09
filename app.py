from flask import Flask, session
from flask_session import Session
from flask_restful import Api
from routes import InitRoutes
from os import environ, path, sep
from app_data.definitions import server_port


app = Flask(__name__)
api = Api(app)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

app.config['APP_PATH'] = path.dirname(__file__)
app.config['UPLOAD_FOLDER'] = app.config['APP_PATH'] + sep + 'dbimages'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 100

InitRoutes(api)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST','localhost')
    PORT = server_port
    app.run(HOST, PORT, debug=True)
    
    # http://localhost:5001/api/v1/hello
    # http://localhost:5001/api/v1/status?deviceId=2