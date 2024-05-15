from lxml import etree

# Load the XML file
xml_file = etree.parse("Hospital.xml")  # Replace with your filename

# Define your XPath or XQuery
while(True):
    xpath_or_xquery = str(input("Enter an X_path or X_Query here \n")).strip()
    # Execute the query
    try:
        if xpath_or_xquery.startswith("//") or xpath_or_xquery.startswith("/"):  # XPath
            result = xml_file.xpath(xpath_or_xquery)
        else:  # XQuery (assuming lxml)
            result = xml_file.xpath(xpath_or_xquery)
    except Exception:
        print("Un Valid Query!")
        continue

    # Process the results (printing here for demonstration)
    if result:
        for item in result:
            print(item.text)  # Access element text
        
        
# /hospital/Departments/Department/dept_name
# //Department[@dept_id='d8']/dept_name

# for $dept in //Department[@dept_id='d8'] return $dept/dept_name

