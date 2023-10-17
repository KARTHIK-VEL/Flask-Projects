# Import necessary modules
from flask import Flask, render_template
# Initialize the Flask app
app = Flask(__name__)
# Route for the root URL ("/")
@app.route('/')
def result():
    # Define a dictionary with subject scores
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    # Render the 'result.html' template and pass the 'result' dictionary to the template
    return render_template('result.html', result=dict)
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
