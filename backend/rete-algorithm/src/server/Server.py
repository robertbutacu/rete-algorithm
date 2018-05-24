import os
from __builtin__ import file
from flask import app, Flask, request, flash, url_for
from werkzeug.utils import redirect, secure_filename

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
    # return build_network(code, False)


@app.route('/file', methods=['POST'])
def graph_from_file():
    def allowed_file(file):
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('uploaded_file', filename=filename))


if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run()
