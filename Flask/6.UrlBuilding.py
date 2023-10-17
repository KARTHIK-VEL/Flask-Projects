# Import necessary modules
from flask import Flask, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Route for the '/admin' URL
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

# Route for the '/guest/<guest>' URL
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest

# Route for the '/user/<name>' URL
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))  # Redirect to hello_admin() function
    else:
        return redirect(url_for('hello_guest', guest=name))  # Redirect to hello_guest() function

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
