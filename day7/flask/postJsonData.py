from flask import Flask, request, jsonify

# app object

app = Flask(__name__)


@app.route('/employee', methods=['POST'])
def welcome():
    data = request.get_json()
    name = data['name']
    email_id = data['email_id']
    return jsonify(
        {
            "name": name,
            "email": email_id
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
