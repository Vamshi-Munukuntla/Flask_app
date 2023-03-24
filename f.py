from flask import Flask

# Initialize the object
app = Flask(__name__)


@app.route('/')
def home():
    return 'this is fucked up'


if __name__ == "__main__":
    app.run()
