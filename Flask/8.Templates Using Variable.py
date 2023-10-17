# Import necessary modules
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Route for the root URL ("/")
@app.route("/")
def index():
    # A multiline string containing the HTML code to be returned
    str = """
<html>
<body>
<h1>Hello World</h1>
</body>
</html>
"""
    return str  # Return the HTML code as the response

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
