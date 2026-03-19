from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,URL=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = URL
    
    def __eq__(self , other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type.value}, {self.url})")

    
def text_node_to_html_node(text_node):
    type = text_node.text_type
    content = text_node.text
    if type == TextType.TEXT:
        return LeafNode(None , content)
    elif type == TextType.BOLD:
        return LeafNode("b" , content)
    elif type == TextType.ITALIC:
        return LeafNode("i" , content)
    elif type == TextType.CODE:
        return LeafNode("code" , content)
    elif type == TextType.LINK:
        return LeafNode("a" , content , {"href":text_node.url} )
    elif type == TextType.IMAGE:
        return LeafNode("img" , "" , {"src":text_node.url , "alt":content})
    else:
        raise Exception("not a valid inline")



    
