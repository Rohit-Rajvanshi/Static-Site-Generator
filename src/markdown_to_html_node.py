from md_to_blocks import *
from htmlnode import *
from splitnodes import *
from textnode import *
from inline_markdown import *




def markdown_to_html_node(markdown):
    markdown_block = markdown_to_blocks(markdown)
    block_node_list = []

    for block in markdown_block:
        
        block_type = block_to_block_type(block)

        if block_type == BlockType.paragraph:
            block_text = block.replace("\n", " ")
            para_child_nodes = text_to_children(block_text)
            block_node_list.append(ParentNode( "p" , para_child_nodes))

        elif block_type == BlockType.heading:
            heading_number = count_hashtags(block)
            block_text = strip_hashtags(block)
            heading_child_nodes = text_to_children(block_text)
            block_node_list.append(ParentNode(f'h{heading_number}' , heading_child_nodes))

        elif block_type == BlockType.code:
            block_text = strip_backticks(block)
            block_node_list.append(ParentNode( "pre" , [LeafNode("code" , block_text)]))

        elif block_type == BlockType.unordered_list:
            ul_child_nodes = unordered_list_split(block)
            block_node_list.append(ParentNode("ul" , ul_child_nodes))

        elif block_type == BlockType.ordered_list:
            ol_child_nodes = ordered_list_split(block)
            block_node_list.append(ParentNode("ol" , ol_child_nodes))

        elif block_type == BlockType.quote:
            quote_child_nodes = strip_quotes(block)
            block_node_list.append(ParentNode("blockquote" , quote_child_nodes))

    div_node = ParentNode("div" , block_node_list)
    return div_node


    



def text_to_children(text):
    split_nodes = text_to_text_nodes(text)
    html_nodes = []
    for split_node in split_nodes:
        html_node = text_node_to_html_node(split_node)
        html_nodes.append(html_node)
    return html_nodes
        


    



def count_hashtags(block):
    for prefix in ("# ", "## ", "### ", "#### ", "##### ", "###### "):
        if block.startswith(prefix):
            return prefix.count("#")


def unordered_list_split(block):
    u_lt = block.split("\n")
    html_nodes = []
    for lt in u_lt:
        lt = lt [2:]
        lt_node = text_to_children(lt)
        html_node = ParentNode("li" , lt_node)
        html_nodes.append(html_node)
    return html_nodes
    


def ordered_list_split(block):
    o_lt = block.split("\n")
    html_nodes = []
    for lt in o_lt:
        index = lt.index(" ") + 1
        lt = lt[index:]
        lt_node = text_to_children(lt)
        html_node = ParentNode("li" , lt_node)
        html_nodes.append(html_node)
    return html_nodes
    
    

def strip_hashtags(block):
    for prefix in ("# ", "## ", "### ", "#### ", "##### ", "###### "):
        if block.startswith(prefix):
            block_text = block.removeprefix(prefix)
    return block_text

def strip_backticks(block):
    block_text = block.removeprefix("```\n")
    block_text = block_text.removesuffix("```")
    return block_text


def strip_quotes(block):
    quote_split_list = block.split("\n")
    clean_quotes = []
    quote_text = ""
    for quote in quote_split_list:
        quote = quote.removeprefix(">") 
        if quote and quote[0] == " ":
            quote = quote.removeprefix(" ")
        clean_quotes.append(quote)

    quote_text = " ".join(clean_quotes)
    return text_to_children(quote_text)
