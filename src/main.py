from copystatic import *
from generate_page import *
import sys 


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    copy_static("static" , "docs")
    generate_page_recursive("content" , "template.html" , basepath)
  
main()
