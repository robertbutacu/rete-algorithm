from flask import app, Flask, request

from src.services.ServerServices import build_network

UPLOAD_FOLDER = 'E:\\Projects\\rete-algorithm\\uploads'
ALLOWED_EXTENSIONS = {'clp'}


app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/clips-code', methods=['POST'])
def graph_for_code():
    code = request.form['code']

    print(code)

    return "welcome"
    #return build_network(code, False)


@app.route('/file', methods=['POST'])
def graph_from_file():
    return None


if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()