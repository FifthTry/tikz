import os
from command import utils as command_utils


class Tikz:
    def __init__(self):
        pass

    def run(self, file_path):
        # Convert the tex file to pdf.
        command = '/usr/bin/pdflatex {} -output-directory={}'.format(
            file_path,
            '/tmp/'
        )
        print(command)
        try:
            output = command_utils.run_command(command)
        except Exception as e:
            print('Exception({}) occurred while running command'.format(e))
            return False
        else:
            print('Tikz run success. Output ({})'.format(output))

        # Convert the generated pdf file to png.
        generated_pdf = file_path.replace('.tex', '.pdf')
        filename = generated_pdf.split('/')[-1]
        command = '/usr/bin/pdftoppm -png {} {}'.format(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                '..', filename
            ),
            generated_pdf.replace('.pdf', '')
        )
        print(command)

        try:
            output = command_utils.run_command(command)
        except Exception as e:
            print('Exception(%s) occurred while running command' % e)
            return False
        else:
            print('Pdf to img conversion success with output({})'.format(output))

        return True
