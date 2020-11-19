import uuid

from flask import Flask, request, send_file
from command import tikz

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/tikz', methods=['POST'])
def tikz_output():
    text = request.data
    print(text)
    if not text:
        return 'Text required'

    # Store data in temp file.
    file_id = str(uuid.uuid4())
    file_path = '/tmp/%s.tex' % file_id
    with open(file_path, 'wb+') as f:
        f.write(text)

    tikz_instance = tikz.Tikz()
    output = tikz_instance.run(file_path=file_path)

    # Get the png file from the tmp.
    if output:
        return send_file(
            '/tmp/%s-1.png' % file_id,
            mimetype='image/png'
        )

    return 'failure'


