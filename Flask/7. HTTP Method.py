# Import necessary modules
from flask import Flask, redirect, url_for, request
# Initialize the Flask app
app = Flask(__name__)
# Route for the '/welcome/<name>' URL
@app.route('/welcome/<name>')
def welcome(name):
    return 'Welcome %s' % name
# Route for the '/login' URL with support for both POST and GET methods
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']  # Retrieve the value of the 'nm' field from the form
        return redirect(url_for("welcome", name=user))  # Redirect to the 'welcome' route with the 'name' parameter
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
