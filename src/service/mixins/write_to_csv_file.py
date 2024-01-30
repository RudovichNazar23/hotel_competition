import csv


class WriteToCsvFile:
    def __init__(self, response_object, headers: list, data):
        self.response = response_object
        self.headers = headers
        self.data = data

    def create_writer(self):
        writer = csv.writer(self.response)
        return writer

    def write_headers(self, writer):
        writer.writerow(self.headers)

    def write_rows(self):
        writer = self.create_writer()

        self.write_headers(writer=writer)

        for row in self.data:
            writer.writerow(row)
