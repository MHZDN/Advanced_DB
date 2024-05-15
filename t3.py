# Test any code here
# from xml.etree import ElementTree as ET
from lxml import etree
from xmlschema import XMLSchema
from xml.etree import ElementTree as ET

global First_entry 

First_entry = True

ele_list = []
# xml_file = etree.parse("Hospital.xml")  # Replace with your filename
# root_element = xml_file.getroot()

xml_tree = ET.parse("Hospital.xml")
xml_root = xml_tree.getroot()

# print(type(tree))
# print(type(xml_file))

# sub_elements = root_element.getchildren()
def recursion(sub_elements):
    for ele in sub_elements:
        print(f"{ele.tag} <{ele.attrib}>: {ele.text}")
        if ele.text.strip() == '' :
            print(True)
        # print(ele.text)
        recursion(ele.getchildren())

def recurse(Element,parent_indx,First_entry): #start with indx -1
   
    children = Element.findall("*")
    d=dict()
    l=list()
    
    # check if there is children
    if children:
        # print(children)
        for child in children:
            if child.tag in d:
                continue
            else:
                # print(type(child.tag))
                d[child.tag] = child  # {name of child : object}
                l.append(child.tag) # [name of child]

    # print(d)
    # print(l)
    for ele in l:

        if d[ele].attrib: # the return is a dictionary
            att_dic=dict()
            for key in d[ele].attrib.keys():
                att= input(f"Enter the value for the attribute: {key} = ").strip()
                att_dic[key] = att

        if d[ele].text.strip() == '':
            # parent_indx = -1
            if (First_entry) and (len(l) == 1):
                print("First_entry here")
                First_entry = False

                if d[ele].attrib:
                    ele_list.append(ET.Element(ele , attrib = att_dic))
                else:
                    ele_list.append(ET.Element(ele))
                new_parent_indx = 0
            else:
                if d[ele].attrib:
                    sub = ET.SubElement(ele_list[parent_indx], ele , attrib = att_dic)
                    ele_list.append(sub)
                    new_parent_indx = ele_list.index(sub)

                else:
                    sub = ET.SubElement(ele_list[parent_indx], ele)
                    ele_list.append(sub)
                    new_parent_indx = ele_list.index(sub)


            recurse(d[ele],new_parent_indx,First_entry)


        #dont forget that text are always the leaf nodes
        else: 
            txt = input(f"Enter the value for the element {ele} = ").strip() 

            if First_entry and len(l) == 1:
                print("First_entry here")
                First_entry = False

                if d[ele].attrib:
                    ELE = ET.Element(ele , attrib = att_dic)
                    ELE.text = txt
                else:
                    ELE = ET.Element(ele)
                    ELE.text = txt

            else:
                if d[ele].attrib:
                    sub = ET.SubElement(ele_list[parent_indx],ele, attrib = att_dic)
                    sub.text = txt
                else:
                    sub = ET.SubElement(ele_list[parent_indx],ele)
                    sub.text = txt

            # sub.text = txt
            # ele_list.append(sub)

    

    

# found_element = xml_root.find("Doctors")

# new_doctor = ET.Element("Doctor", attrib={"doctor_id": "d15" , "dept_id":"d9"})

# new_department_name = ET.SubElement(new_department, "dept_name")

# new_department_name = ET.SubElement(new_department, "dept_name")
# new_department_name.text = "Anesthesiology"

# print(found_element)
# recurse(found_element,-1,First_entry)

# found_element.append(ele_list[0])
print(xml_root.find("Doctors"))
# xml_tree.write("H.xml")



