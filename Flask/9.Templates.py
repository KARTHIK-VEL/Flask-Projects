# Import necessary modules
from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Route for the root URL ("/")
@app.route("/")
def index():
    return render_template('hello.html')  # Render the 'hello.html' template

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()

