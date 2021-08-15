from flask import Flask, current_app




app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    return current_app.send_static_file('pages/index.html')


