# Import necessary modules
from flask import Flask, render_template, request

# Initialize the Flask app
app = Flask(__name__)

# Route for the root URL ("/")
@app.route("/")
def student():
    return render_template('student.html')  # Render the 'student.html' template

# Route for the '/result' URL with POST and GET methods
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form  # Get the form data
        return render_template("result.html", result=result)  # Render the 'result.html' template

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
