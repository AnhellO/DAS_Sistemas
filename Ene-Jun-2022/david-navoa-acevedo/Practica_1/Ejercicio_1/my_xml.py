import xml.etree.cElementTree as ET

from numpy import euler_gamma

xml = 'sample.xml'

#Read xml only function
def read_xml(xml):
    tree = ET.parse(xml)
    root = tree.getroot()
    return root

#Print pair ID only people function
def print_pair_id(root_Element):

    elem_dict = []

    for each in root_Element.iter('id'):
        if (id % 2) == 0:
            elem_dict.append(each)

    print(*elem_dict, sep = '\n')

#Print .edu and .gov email domain people function
def print_edu_gov_dom(root_element):
    
    elem_dict = []

    for each in root_element.iter('email'):
        temp_str = ''
        temp_str = each.attrib

        if temp_str.find('.gov') != -1 or temp_str.find('.edu') != -1:
            elem_dict.append(each)

    print(*elem_dict, sep = '\n')

#Modify ip address to a constant one function
def modif_ip_address(root_element):
    
    for each in root_element.iter('id'):
        each.text = '127.0.0.1'
