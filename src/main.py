from copystatic import *
from generate_page import *


def main():

  
    copy_static("static" , "public")
    generate_page_recursive("content" , "template.html" , "public")
  
main()