"""
Test the app module.
Author: Wolf Paulus (wolf@paulus.com)
"""
from unittest import TestCase
from streamlit.testing.v1 import AppTest
from app import ui, is_website_up
import requests

    
class Test(TestCase):
    def test_ui_title_and_header(self):
        # at = AppTest.from_file("./src/app.py")
        # at.run()
        pass
        # assert at.title[0].value.startswith("URL")
        # assert at.subheader[0].value.startswith("Enter")
        # # assert not at.exception
        # assert is_website_up("https://en.wikipedia.org/wiki/List_of_countries_by_real_GDP_growth_rate")
