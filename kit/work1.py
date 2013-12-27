import sys,string
from xml.dom.minidom import parseString, parse
dom = parse('input.xml')
nodeList = dom.childNodes
nodeboot = dom.createElement("boot")
nodeboot.setAttribute('dev','hd')
for node in nodeList:
    if node != None and node._get_localName() == "domain":
        children = node._get_childNodes()
        for node1 in children:
            if node1 != None and node1._get_localName() == "os":
                children2 = node1._get_childNodes()
                for node2 in children2:
                    if node2 != None and node2._get_localName() in ["kernel","initrd"]:
                        node3= node1.removeChild(node2)	
                node1.appendChild(nodeboot)						
file = open('output.xml','w')
file.write(dom.toxml())
file.close()