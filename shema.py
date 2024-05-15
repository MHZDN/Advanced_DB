from xmlschema import XMLSchema

# Assuming you have an XSD schema file named "hospital.xsd"
schema = XMLSchema("Hospital.xsd")

def get_required_attributes(element_name):
    element = schema.elements.get(element_name)
    if element is None:
        return None
    return list(element.attributes)

element_name = "Doctor"  # Replace with the element you're interested in
required_attrs = get_required_attributes(element_name)
# print(required_attrs)

# print(type(required_attrs[0]))

# if required_attrs:
#     print(f"Required attributes for '{element_name}': {', '.join(required_attrs)}")
# else:
#     print(f"No required attributes defined for '{element_name}' in the XSD schema.")