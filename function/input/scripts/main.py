"""
This script reads the varname.yaml for rtsp and 
register the rtsp links in the index.js with the 
endpoint being the key from the list.

Also, it stubs javascript codes in the status.html 
to load the rtsp streams

Usage: python main.py
"""
import sys
import yaml
from string import Template


varname_data = None
with open("varname.yaml", 'r') as stream:
    try:
        varname_data = yaml.load(stream, Loader=yaml.Loader)
    except yaml.YAMLError as exc:
        print(exc)

style_data = None
with open("style.yaml", 'r') as stream:
    try:
        style_data = yaml.load(stream, Loader=yaml.Loader)
    except yaml.YAMLError as exc:
        print(exc)


def main(arguments):
    
    plugin_type = arguments[0]


    with open("./bora/status.html", "r") as f:
        contents = f.readlines()
     
    # stub code
    anchor = 0
    for num, line in enumerate(contents):
        if "<!-- BORA START -->" in line:
            anchor = num
            break
    anchor += 1

    #### 01. LOAD PLUGIN TEMPLATE
    with open("./bora/template/" + plugin_type + ".html", "r") as f:
        status_template_stub = f.readlines()
    
    for num, line in enumerate(status_template_stub):
        contents.insert(anchor+num, line)

    with open("./bora/status.html", "w") as f:
        contents = "".join(contents)
        f.write(contents)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
