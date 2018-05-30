import os

from flask import Flask, request, flash, url_for, session, jsonify, json, abort
from werkzeug.utils import redirect, secure_filename

from src.services.ServerServices import build_network, get_example_service
from src.services.TransformerServices import print_network

UPLOAD_FOLDER = 'E:\\Projects\\rete-algorithm\\uploads'
ALLOWED_EXTENSIONS = {'clp'}

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/clips-code', methods=['POST'])
def graph_for_code():
    if request.headers['Content-Type'] == 'application/json':
        try:
            message = request.get_json()
            network = build_network(message["code"], False)

            network_as_dict = network.to_dict()
            resp = jsonify(network_as_dict)
            resp.status_code = 200
            return resp
        except Exception:
            abort(400)

    return redirect(request.url)


@app.route('/file', methods=['POST'])
def graph_from_file():
    def allowed_file(file):
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    try:
        file = request.files['inputFile']

        if file.filename == '':
            flash('No selected file')
            print("FILENMAE NAME IS FKING NAKED")
            return redirect(request.url)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        print("Trying to build network")
        network = build_network(filepath, True)
        print("Finished building network")
        network_as_dict = network.to_dict()
        resp = jsonify(network_as_dict)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        return redirect(request.url)


@app.route('/example/<example>', methods=['POST'])
def get_example(example):
    return jsonify(get_example_service(example).to_dict())


if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
