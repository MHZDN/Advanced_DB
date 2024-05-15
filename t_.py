from xml.etree import ElementTree as ET

def add_new_doctor(xml_file, doctor_data):
  """
  This function adds a new doctor element to the "Doctors" element in an XML file.

  Args:
      xml_file: The path to the XML file (string).
      doctor_data: A dictionary containing doctor information (all attributes and nested elements).
  """
  # Parse the XML file
  tree = ET.parse(xml_file)
  root = tree.getroot()

  # Find the "Doctors" element
  doctors_element = root.find("Doctors")

  # Create a new doctor element
  new_doctor = ET.Element("Doctor")

  # Add attributes to the new doctor element
  for key, value in doctor_data.get("attributes", {}).items():
    new_doctor.set(key, value)

  # Add nested elements for details (name, speciality, contact details)
  name_element = ET.SubElement(new_doctor, "doctor_name")
  name_sub_element = ET.SubElement(name_element, "First_name")
  name_sub_element.text = doctor_data.get("name", {}).get("first_name", "")
  name_sub_element = ET.SubElement(name_element, "Last_name")
  name_sub_element.text = doctor_data.get("name", {}).get("last_name", "")

  speciality_element = ET.SubElement(new_doctor, "speciality")
  speciality_element.text = doctor_data.get("speciality", "")

  contact_details_element = ET.SubElement(new_doctor, "contact_details")
  contact_sub_element = ET.SubElement(contact_details_element, "Email")
  contact_sub_element.text = doctor_data.get("contact_details", {}).get("email", "")
  contact_sub_element = ET.SubElement(contact_details_element, "phone_number")
  contact_sub_element.text = doctor_data.get("contact_details", {}).get("phone_number", "")

  # Append the new doctor element to the "Doctors" element
  doctors_element.append(new_doctor)

  # Write the modified XML data to the file
  tree.write(xml_file)

# Example usage
doctor_data = {
  "attributes": {
    "doctor_id": "DOC1005",
    "dept_id": "DEPT002"
  },
  "name": {
    "first_name": "John",
    "last_name": "Smith"
  },
  "speciality": "Cardiology",
  "contact_details": {
    "email": "john.smith@hospital.com",
    "phone_number": "+1234567890"
  }
}

# Replace 'hospital.xml' with your actual filename
add_new_doctor("Hospital.xml", doctor_data)

print("New doctor added successfully!")
