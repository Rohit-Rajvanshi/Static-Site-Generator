

def extract_title(markdown):
    markdown_block = markdown.split("\n")
    title=""
    for md in markdown_block:
        if md[0:2] == "# ":
            title = md.replace("#" , "", 1)
            title = title.strip(" ")
            break
    if not title:
        raise Exception("No title found")

    
    return title 


