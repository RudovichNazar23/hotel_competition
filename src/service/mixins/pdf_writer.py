from weasyprint import HTML
import tempfile


class PdfWriter:
    def __init__(self, html_string, response_object):
        self.html_string = html_string
        self.response_object = response_object

    def create_html_object(self):
        html = HTML(string=self.html_string)
        return html

    def write_data(self):
        html_object = self.create_html_object()

        result = html_object.write_pdf()

        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()

            output = open(output.name, "rb")
            self.response_object.write(output.read())
