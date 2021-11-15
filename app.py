from flask import Flask, request
from Model.ForestryManager.ForestriesRESTController import forestries_controller
from conf import AUTH_PASS, AUTH_LOGIN
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(forestries_controller)
CORS(app)


def check_auth(username, password):
    return username == AUTH_LOGIN and password == AUTH_PASS


@app.before_request
def before_request():
    auth = request.authorization
    if not (auth and check_auth(auth.username, auth.password)):
        return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()
