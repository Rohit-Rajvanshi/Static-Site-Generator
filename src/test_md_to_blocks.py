import unittest
from md_to_blocks import *

class TestMD(unittest.TestCase):
    def test_block_to_block_type(self):
        md = "# This is **bolded** paragraph"
  
        output = block_to_block_type(md)
        self.assertEqual(output , BlockType.heading)
        
        

if __name__ == "__main__":
    unittest.main()
