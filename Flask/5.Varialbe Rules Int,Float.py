# Import necessary modules
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the root URL ("/")
@app.route("/")
def hello():
    return 'Hello'
# Define a dynamic route with an integer parameter
@app.route('/int/<int:name>')
def int_route(name):
    return 'Int %d!' % name
# Define a dynamic route with a float parameter
@app.route('/float/<float:name>')
def float_route(name):
    return 'Float %f!' % name
@app.route('/path/')
def path_route():
    return 'path'

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
