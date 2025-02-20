import json
import unittest

from secscanner2junit import SastParser
from secscanner2junit.config import get_config


class TestSast(unittest.TestCase):

    def test_sast_suppression(self):
        # given:
        input_report_path = "resources/test_sast/test_sast_suppression/gl-sast-report-many-with-same-name.json"
        input_config_path = "resources/test_sast/test_sast_suppression/ss2ju-config.yml"

        report = get_report(input_report_path)
        config = get_config(input_config_path)
        parser = SastParser(report, input_report_path, config)

        # when:
        testsuite = parser.parse()

        # then:
        self.assertEqual(len(testsuite.pop().test_cases), 2)


def get_report(path):
    with open(path) as input_file:
        return json.load(input_file)
