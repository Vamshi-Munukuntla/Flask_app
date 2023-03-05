from flask import Flask

# Initialize the object
app = Flask(__name__)


@app.route("/Vamshi")  # localhost: port_number
def home():
    return 'this is our first flask application'


if __name__ == '__main__':
    app.run(debug=True)  # port_number, options, host
