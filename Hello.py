from flask import Flask
app = Flask(__name__)

@app.route('/')
def view_function():
  return '<h1>Hello, World! its me Dema.</h1>'
