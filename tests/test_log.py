"""
Test the log module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from os.path import getsize
import yaml
from unittest import TestCase
from log import logger as log


class Test(TestCase):
    def test_log_to_file(self):
        with open('./src/logconfig.yaml', 'r') as f:
            config = yaml.safe_load(f.read())
        log_file_name = config["handlers"]["file"]["filename"]
        file_size = getsize(log_file_name)
        log.error("This it not an error, justing testing the log module.")
        assert file_size < getsize(log_file_name)
