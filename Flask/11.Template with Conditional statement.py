# Import necessary modules
from flask import Flask, render_template
# Initialize the Flask app
app = Flask(__name__)
# Route for the '/marks/<int:score>' URL
@app.route('/marks/<int:score>')
def index(score):
    return render_template('hello2.html', marks=score)  # Render the 'hello2.html' template with the 'marks' variable
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
