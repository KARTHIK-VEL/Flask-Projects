# Import necessary modules
from flask import Flask
# Initialize the Flask app
app = Flask(__name__)
# Define the route for the root URL ("/")
@app.route("/")
def hello():
    return 'Hello'
# Define a dynamic route with a parameter
@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
