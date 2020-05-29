from flask import Flask

# app object

app = Flask(__name__)


@app.route('/')
def welcome():
    print("welcome")
    return 'Welcome To Teckat'


@app.route('/user')
def user():
    return "Hello User"


if __name__ == "__main__":
    app.run(debug=True)
