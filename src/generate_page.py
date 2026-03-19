from markdown_to_html_node import *
from htmlnode import *
from extract_title import *
import os


def generate_page(from_path , template_path , dest_path ,basepath):
    print (f'Generating page from {from_path} to {dest_path} using {template_path}')

    folder_name = os.path.dirname(dest_path)
    if folder_name != "":
        os.makedirs(folder_name , exist_ok = True)

    with open(from_path , "r") as md_file:
        content = md_file.read()

    with open(template_path , "r") as md_file:
        template_content = md_file.read()

    nodes = markdown_to_html_node(content)
    html = nodes.to_html()
    title = extract_title(content)

    template_content = template_content.replace("{{ Content }}" , html)
    template_content = template_content.replace("{{ Title }}" , title)
    template_content = template_content.replace('href="/' , f'href="{basepath}')
    template_content = template_content.replace('src="/' , f'src="{basepath}' )



    with open(dest_path , "w") as html_file:
        html_file.write(template_content)
        html_file.close()


def generate_page_recursive(dir_path_content , template_path , dest_dir_path , basepath):
        def md_files_extract(dir_path_content , dest_dir_path):
            content_files = os.listdir(dir_path_content)
            for content in content_files:
                content_path = os.path.join(dir_path_content , content)
                destination_path = os.path.join(dest_dir_path , content)
                if os.path.isfile(content_path) and content.endswith(".md"):
                    destination_path = destination_path.replace(".md" , ".html")
                    generate_page(content_path , template_path , destination_path , basepath)
                elif os.path.isdir(content_path):
                    if not os.path.isdir(destination_path):
                        os.makedirs(destination_path , exist_ok=True)
                    md_files_extract(content_path , destination_path)
        md_files_extract(dir_path_content , dest_dir_path)




    