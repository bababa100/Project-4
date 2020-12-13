from flask import Flask, jsonify, g

import models

DEBUG = True
PORT = 8000

# Initiallize instance of the Flask class
# Starts the website
app = Flask(__name__)

# g stands for global - for setting up
# global access to our database throughout the app.


@app.before_request
def before_request():
    "Connect to the database before each request."
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    "Close the database connection after each response."
    g.db.close()
    return response
# The default URL ends in / ("my-website.com/").


@app.route('/')
def index():
    # This is what will display
    return 'hi'


# @app.route('/json')
# def student():
#     return jsonify(name="Jake", age=28)


# @app.route('/sayhi/<username>')
# def hello(username):
#     return "Hello {}" .format(username)


# Run the app when the program starts:
if __name__ == '__main__':
    print('tables connected')
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
