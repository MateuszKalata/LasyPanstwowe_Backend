from flask import Flask, request, make_response
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
def after_request_func(response):
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    app.run()
