import os
from flask import Flask, request, send_file
from subprocess import Popen, PIPE, TimeoutExpired

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


def run_command(cmd, timeout=40):
    print("Running command %s" % (cmd))
    with Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True) as ps_process:
        try:
            success, err = ps_process.communicate(timeout=timeout)
            if success or not err:
                success = 'true'
            print('Command(%s) Error(%s)' % (cmd, err))
        except TimeoutExpired as e:
            print("TimeoutException " + str(e))
            ps_process.kill()
            success = "Timeout"
        except Exception as e:
            print("Exception " + str(e))
            ps_process.kill()
            success = "Exception"

    return success


def read_file(name, mode='r'):
    return open(name, mode).read().strip()


@app.route('/simple', methods=['POST'])
def simple():
    open(
        read_file('file.txt'),
        mode="wb"
    ).write(
        bytes(request.form.get('body_data', ''), 'utf-8')
    )

    run_command(read_file('cmd.txt'))
    return send_file(
        read_file("output.txt"),
        mimetype=read_file("mime.txt")
    )


@app.route('/')
def code():
    with open('sample-text.txt') as file_data:
        code = file_data.read()
    return f"""
        <html>
            <body>
                <form action='/simple' method="POST" id="form1">
                    <textarea name="body_data" style="height: 500px; width: 500px;" form="form1" >{str(code)}</textarea>
                    <br />
                    <input type="submit" >
                </form>
            </body>
        </html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
