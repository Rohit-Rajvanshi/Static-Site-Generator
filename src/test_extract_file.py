from extract_title import *
import unittest



class TestMDtoHTML(unittest.TestCase):
    def test_extract_file(self):
        markdown = """
# Lol This title bro 

hey nigga

# this another one lol
"""
        output = extract_title(markdown)

        self.assertEqual(output , "Lol This title bro")


