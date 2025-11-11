from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world from Rex in CSPB 3308'
