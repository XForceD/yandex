import sys,string
from xml.dom.minidom import parseString, parse
from xml.etree import ElementTree as ET
dom = parse('input.xml')
tree = ET.parse('input.xml')
root = tree.getroot()
cmdline=root.find('qemu\\:commandline')
root.remove(cmdline)
elboot = ET.Element('boot')
elboot.attrib['dev']='hd'
for os in root.findall('os'):
    kernel = os.find('kernel')
    initrd = os.find('initrd')
    for boot in os.findall('boot'):
        os.remove(boot)
    bootmenu=os.find('bootmenu')
#    bootloader=os.find('bootloader')	
    os.remove(bootmenu)
#    os.remove(bootloader)	
#    loader=os.find('loader')
#    os.remove(loader)
    os.remove(kernel)
    os.remove(initrd)
    os.append(elboot)
tree.write('output.xml')	
