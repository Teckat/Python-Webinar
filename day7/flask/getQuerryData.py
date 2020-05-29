from flask import Flask, request

# app object

app = Flask(__name__)


@app.route('/employee', methods=['GET'])
def welcome():
    name = request.args.get('name')
    email = request.args.get('email')

    return "name: {}, email: {}".format(name, email)


if __name__ == "__main__":
    app.run(debug=True)
