import csv
from jinja2 import Environment, FileSystemLoader

fsload = loader=(FileSystemLoader('.'))
jinENV = Environment(loader=(fsload))

template = jinENV.get_template("switchconf.j2")

# Use the open method to open the CSV file in read-only-mode
csv_file = open("ports.csv", "r",)
 
# Create the CSV reader object
csv_reader = csv.reader(csv_file)
  
# Create the header object, advance the CSV reader to the header line by using the next() method
header = next(csv_reader)
   
# Search the headers for specifics strings and store
interface = header.index("interface")
description = header.index("description")
vlan = header.index("vlan")

for row in csv_reader:

    interface_dict = {}

    interface_dict["name"] = row[interface]
    interface_dict["description"] = row[description]
    interface_dict["vlan"] = row[vlan]
    interface_dict["uplink"] = False

    print(template.render(interface=interface_dict))
