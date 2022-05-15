from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Ez lesz a Baj22156465or! :-)"
