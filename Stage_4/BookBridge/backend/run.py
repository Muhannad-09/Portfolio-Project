from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {'message': 'BookBridge Backend is running!'}

if __name__ == '__main__':
    # Listen on all interfaces so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
