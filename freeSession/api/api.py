from flask import Flask

# Create app object

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello"


@app.route('/user')
def user():
    return "Teckat"


@app.route('/name/<name>')
def name(name):
    print(name)
    return name


if __name__ == "__main__":
    app.run(debug=True)
