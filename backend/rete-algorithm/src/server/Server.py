import os

from flask import Flask, request, flash, url_for, session
from werkzeug.utils import redirect, secure_filename

from src.services.ServerServices import build_network
from src.services.TransformerServices import print_network

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
    # return build_network(code, False)


@app.route('/file', methods=['POST'])
def graph_from_file():
    def allowed_file(file):
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    file = request.files['inputFile']

    if file.filename == '':
        flash('No selected file')
        print("FILENMAE NAME IS FKING NAKED")
        return redirect(request.url)
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    network = build_network(filepath, True)
    print_network(network.states)
    print(network.text)
    return redirect(request.url)


''' if file and allowed_file(file.filename):
     file.save(os.path.join("E:\\", file))
     return redirect(url_for('uploaded_file', filename=file))
'''

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
