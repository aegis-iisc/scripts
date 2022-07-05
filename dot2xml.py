from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import os
import sys
 
# Can't locate the write_json functionality in pydot or pydotplus although present in 
#cli for dot thus directly using the dot cli in a system process.
# Feel free to make changes as I have been writing Python after a loooong gap.

# import pydot
# graphs = pydot.graph_from_dot_file('test.dot')
# graph = graphs[0]
#graph.write_png("test1.png")

# Usage dot2xml dotfilepath
def main():
    
# total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)
    if n != 2:
        sys.exit("Invalid Usage")
    else:
        dotfile = sys.argv[1] 
        output = dotfile+".json"
        os.system ("dot -Txdot_json  -o "+output+" "+dotfile)
        # get the data from an URL
        data = readfromjson(output)
        print(json2xml.Json2xml(data).to_xml())


if __name__ == '__main__':
   main()  # next section explains the use of sys.exit