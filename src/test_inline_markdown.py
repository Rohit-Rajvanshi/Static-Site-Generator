import unittest
import re
from inline_markdown import *



class TestMDImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_links(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(matches , [("image", "https://i.imgur.com/zjjcJKZ.png")])

if __name__ == "__main__":
    unittest.main()

