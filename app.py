from waitress import serve 
from flask import Flask, current_app



app = Flask(__name__)

if __name__ == "__main__":
    serve(app)

@app.route("/")
def mhomepage():
    return current_app.send_static_file('pages/index.html')

@app.route("/tableau")
def my_tableau_page():
    # return "<p>Hello, World!</p>"
    return current_app.send_static_file('pages/tableautest.html')


