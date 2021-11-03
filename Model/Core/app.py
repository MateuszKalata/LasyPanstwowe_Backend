from flask import Flask
 
app = Flask(__name__)
 
@app.route("/")
def home_view():
        return None
 
if __name__ == "__main__":
        app.run()
