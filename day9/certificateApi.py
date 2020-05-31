from flask import Flask, request
from function import generateCerti as certifiy
# app object

app = Flask(__name__)


@app.route('/employee/certificate', methods=['POST', 'GET'])
def certificate():
    if request.method == 'POST':
        newName = request.args.get('name')
        num = request.args.get('certiNum')
        data = request.get_json()
        name = data['name']
        certiNum = data['certiNum']
        print(name, certiNum)
        certifiy.certificate(certiNum, name)
        return "{}, {},{},{}".format(name, certiNum, newName, num)
    else:
        return "the method is get"


if __name__ == "__main__":
    app.run(debug=True)
