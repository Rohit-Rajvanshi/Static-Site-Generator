from htmlnode import *
import unittest
from textnode import *


class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_nodes(self):
        node_1  = LeafNode("b", "node_1")
        node_2 = LeafNode("span" , "node_2")
        node_3 = ParentNode("div", [node_1 , node_2])
        node_4 = ParentNode("p", [node_3])
        self.assertEqual(
            node_4.to_html(),
            "<p><div><b>node_1</b><span>node_2</span></div></p>",
        )

    
    
        

if __name__ == "__main__":
    unittest.main()

