from xml.etree import ElementTree as ET
from lxml import etree
from xmlschema import XMLSchema

First_entry = True
ele_list = []

def load_xml(filename):
    try:
        # why because each library has things the others doesnt have
        xml_tree = ET.parse(filename)
        xml_root = xml_tree.getroot()
        lxml_tree = etree.parse(filename)
        lxml_root = lxml_tree.getroot()

        return xml_tree, xml_root ,lxml_tree, lxml_root
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None, None, None



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
                d[child.tag] = child  # {name of child : object}
                l.append(child.tag) # [name of child]

    for ele in l:

        if d[ele].attrib: # the return is a dictionary
            att_dic=dict()
            for key in d[ele].attrib.keys():
                att= input(f"Enter the value for the attribute: {key} = ").strip()
                att_dic[key] = att

        if d[ele].text.strip() == '':
            
            if (First_entry) and (len(l) == 1):

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



def add_entry(First_entry,ele_list):

    """
    """
    condition =True
    while condition:

        Element=input("Please Enter the ELement name you want to add in : ").strip()
        found_element = xml_root.find(Element)
        if found_element == None:
            print(f"The Element '{Element}' is not found!")
            continue
        else:
            recurse(found_element,-1,First_entry)
            found_element.append(ele_list[0])
            xml_tree.write(f"{plain_name}_modified.xml")
            print(f"Element has been succefully added to {Element}!\n")
            ele_list=[]
            First_entry = True

        while(True):
            choice = input("Do you Like to add another Element? [y/n]")
            if choice.lower().strip() =='y':
                break
            elif choice.lower().strip() =='n':
                condition = False
                break
            else:
                print("Invalid choice!")

# def delete_entry():
#     condition = True
#     while(condition):
#         element_tag = input("Please enter the Element Tag you want to delete from  ").strip()
#         if xml_root.findall(element_tag):
#             # element_id =  input("Please enter the Element ID to to be deleted  ").strip()
#             try:
#                 for element in xml_root.findall(element_tag):
#                     if element.attrib:
#                         for ele in element.attrib.keys():
#                             if element.get(ele) == element_id:
#                                 xml_root.remove(element)
#                                 xml_tree.write("Hospital_modified.xml")  # Write to a new file
#                                 print(f"Entry in '{element_tag}' with ID:'{element_id}' successfully deleted!")                        
#                 # print(f"Error: Entry with ID '{element_id}' not found.")
#             except Exception as e:
#                 print(f"Error deleting entry: {e}")
#         else:
#             print(f"The Element {element_tag} you want to delete from is not found! ")

#         while(True):
#             choice = input("Would you Like to Delete Agian [y/n]")
#             if choice.lower().strip() =='y':
#                 break
#             elif choice.lower().strip() =='n':
#                 condition = False
#                 break
#             else:
#                 print("Invalid choice!")


def query_recursion(items):
    
    for item in items:
        if item.text.strip() == '':
            if item.attrib:
                print(f"{item.tag} <{item.attrib}> :")
            else:
                print(f"{item.tag}:")
            query_recursion(item.findall("*"))
        else:
            print(f"{item.tag} : {item.text}")
    print("--------------")


def query_entry(xpath_or_xquery,xml_file):

    condition = True

    while(condition):
        try:
            if xpath_or_xquery.startswith("//") or xpath_or_xquery.startswith("/"):  # XPath
                result = xml_file.xpath(xpath_or_xquery)
            # else:  # XQuery (assuming lxml)
            #     result = xml_file.xpath(xpath_or_xquery)
        except Exception:
            print("Un Valid Query!")
            return
        
        if result:
                query_recursion(result)
                    # print(item.text)  # Access element text
        print("\n")

        while(True):
            choice = input("Would you Like to query Agian [y/n]")
            if choice.lower().strip() =='y':
                xpath_or_xquery = str(input("Enter another Query Please")).strip()
                break
            elif choice.lower().strip() =='n':
                condition = False
                break
            else:
                print("Invalid choice!")

# Main program flow
plain_name = "Hospital"
filename = "Hospital.xml"  # Replace with your actual filename
schema = "Hospital.xsd" 
xml_tree, xml_root, lxml_tree, lxml_root = load_xml(filename)

if xml_tree is not None:
    while True:
        print("Choose the operation:")
        print("press 'd' to Delete an element from the tree" )
        print("press 'w' to Write an element in the tree")
        print("press 'q' to Query an element from the tree")
        print("press '!' to Close")

        operation = input().strip()

        if operation.lower() == 'q':
            query=str(input("please enter an xQuery or xPath for query : \n")).strip()
            query_entry(query,lxml_tree)


        # elif operation.lower() == 'd':
        #     delete_entry()

        elif operation.lower() == 'w':
            add_entry(First_entry,ele_list)

        elif operation.lower() == '!':
            break
        else:
            print("Invalid choice!")

print("Exiting...")

# //hospital/Departments/Department/dept_name
# //Department[@dept_id='d8']/dept_name

   

