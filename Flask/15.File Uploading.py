# Import necessary modules
from flask import Flask, render_template, request
# Initialize the Flask app
app = Flask(__name__)
# Route for the root URL ("/")
@app.route('/')
def main():
    return render_template("index1.html")  # Render the 'index1.html' template
# Route for the '/success' URL with POST method
@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']  # Get the uploaded file
        f.save(f.filename)  # Save the uploaded file to the server
        return render_template("Acknowledgement.html", name=f.filename)  # Render the 'Acknowledgement.html' template
# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
