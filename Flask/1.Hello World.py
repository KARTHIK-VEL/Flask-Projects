# Import necessary modules
from flask import Flask
# Initialize the Flask app
app = Flask(__name__)
# Define the route for the home page
@app.route('/')
def hello_world():
    return 'Hello World'
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
