import os
from django.test import TestCase
from ..parser import Parser


class ParserTestCase(TestCase):

    def test_parse_response(self):
        response_data = "%s/data/response.html" % os.path.dirname(os.path.realpath(__file__))
        with open(response_data, 'r') as data_file:
            data = "\n".join(data_file.readlines())

        parser = Parser()
        schedule = parser.parse_schedule(data)
        print(schedule)