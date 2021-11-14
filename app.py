from flask import Flask
from Model.ForestryManager.ForestriesRESTController import forestries_controller

app = Flask(__name__)
app.register_blueprint(forestries_controller)

if __name__ == "__main__":
    app.run()
