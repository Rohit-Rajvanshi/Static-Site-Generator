from textnode import *
from inline_markdown import * 

def split_nodes_delimiter(old_nodes , delimiter , text_type):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT :
            new_nodes.append(node)
            continue 

        delimiter_count = node.text.count(delimiter)
        if delimiter_count%2 != 0:
            raise Exception("invalid Markdown Syntax")

        temp_list = node.text.split(delimiter)
        for index in range (0,len(temp_list)):
            if temp_list[index] == "":
                continue 
            elif index % 2 == 0:
                new_nodes.append(TextNode(temp_list[index] , TextType.TEXT))
            else:
                new_nodes.append(TextNode(temp_list[index] , text_type))
                
    return new_nodes

        
def split_nodes_image(old_nodes):
    new_nodes = []


    for node in old_nodes:
        if node.text_type != TextType.TEXT :
            new_nodes.append(node)
            continue 


        matches = extract_markdown_images(node.text)
        if not matches :
            new_nodes.append(node)
            continue 
        node_text = node.text
        for match in matches:
            image_alt = match[0]
            image_link = match[1]
            

            temp_list = node_text.split(f'![{image_alt}]({image_link})', 1)
            for index in range(3):
                if index == 0 and temp_list[0] != "":
                    new_nodes.append(TextNode(temp_list[0], TextType.TEXT))
                elif index == 1:
                    new_nodes.append(TextNode(image_alt , TextType.IMAGE , image_link))
            node_text = temp_list[1]

        if node_text != "":
            new_nodes.append(TextNode(node_text , TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []


    for node in old_nodes:
        if node.text_type != TextType.TEXT :
            new_nodes.append(node)
            continue 

        matches = extract_markdown_links(node.text)
        if not matches:
            new_nodes.append(node)
            continue 
        
        node_text = node.text
        for match in matches:
            link_alt = match[0]
            link_url = match[1]

            

            temp_list = node_text.split(f'[{link_alt}]({link_url})', 1)
            for index in range(3):
                if index == 0 and temp_list[0] != "":
                    new_nodes.append(TextNode(temp_list[0], TextType.TEXT))
                elif index == 1:
                    new_nodes.append(TextNode(link_alt , TextType.LINK , link_url))

            node_text = temp_list[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text , TextType.TEXT))

    return new_nodes

        
def text_to_text_nodes(text):
    text_node = split_nodes_delimiter([TextNode(text , TextType.TEXT)] , "**" , TextType.BOLD)
    text_node = split_nodes_delimiter(text_node , "_" , TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node , "`"  , TextType.CODE)
    text_node = split_nodes_image(text_node)
    text_node = split_nodes_link(text_node)
    

    return text_node
    
    



        

    
