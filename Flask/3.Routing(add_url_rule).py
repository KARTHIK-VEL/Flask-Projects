# Import necessary modules
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def index():
    return 'Welcome to home page'

# Define a route '/hello'
@app.route('/hello')
def hello():
    return 'Hello BIT'l
# Define a function for the 'about' page
def about():
    return 'My home page'
# Add a custom URL rule for '/home'
app.add_url_rule('/home', 'home', about)

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
