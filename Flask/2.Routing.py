from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to home page'

@app.route('/hello')                 #####
def hello():
    return 'Hello BIT'

if __name__ == '__main__':
    app.run()