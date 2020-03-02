from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '''Hello World'''


@app.route('/post-example', methods=['POST'])
def post_example():
    response = request.json

    if response is not None:
        return response

    return "Failed Post Request"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
