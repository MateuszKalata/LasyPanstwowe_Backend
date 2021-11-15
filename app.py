from flask import Flask, request
from Model.ForestryManager.ForestriesRESTController import forestries_controller
from conf import AUTH_PASS, AUTH_LOGIN


app = Flask(__name__)
app.register_blueprint(forestries_controller)


def check_auth(username, password):
    return username == AUTH_LOGIN and password == AUTH_PASS


@app.before_request
def before_request():
    auth = request.authorization
    if not (auth and check_auth(auth.username, auth.password)):
        return 'Unauthorized', 401


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


if __name__ == "__main__":
    app.run()
