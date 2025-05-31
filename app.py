from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"


if __name__ == '__main__':
    # Bind to 0.0.0.0 so it's accessible from outside the container
    app.run(debug=True, host='0.0.0.0')