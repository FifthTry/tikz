import uuid

from flask import Flask, request, send_file
from command import tikz, utils
from command.utils import run_command

app = Flask(__name__)


# @app.route('/simple', methods=['POST'])
# def simple():
#     open(
#         open('file.txt').read().strip(), 'w'
#     ).write(request.data)
#
#     # Run the command
#     output = run_command(
#         open('cmd.txt').read().strip()
#     )
#
#     return send_file(
#         open('output.txt').read().strip(),
#         mimetype=open('mime.txt').read().strip()
#     )
@app.route('/simple', methods=['POST'])
def simple():
    """
    Simple API which will capture the request.data
    and return the output from the file.
    :return:
    """
    # Write the request body into temp file.
    with open('file.txt') as request_file:
        request_file_name = request_file.read().strip()
        with open(request_file_name, 'wb') as request_file_body:
            request_file_body.write(request.data)

    # Get the command to be executed and execute it.
    with open('cmd.txt') as cmd_file:
        # Run provided command.
        command = cmd_file.read().strip()
        print("Inititing the execution for the command {}".format(command))
        utils.run_command(command)
        print("Executed command {} for request data {}".format(
            command, request.data
        ))

    # Get the output of the command executed and return it.
    with open('output.txt') as output_file:
        output_file_name = output_file.read().strip()
        # Get mimetype to be returned from file.
        with open('mime.txt') as mime_text_file:
            mime_text = mime_text_file.read().strip()
            return send_file(
                output_file_name,
                mimetype=mime_text
            )

    return "failure"


if __name__ == '__main__':
    app.run()
