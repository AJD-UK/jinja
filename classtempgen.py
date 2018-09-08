import csv
from jinja2 import Environment, FileSystemLoader

fsload = loader=(FileSystemLoader('.'))
ENV = Environment(loader=(fsload))

template = ENV.get_template("switchconf.j2")

# Use the open method to open the CSV file in read-only-mode
csv_file = open("ports.csv", "r",)
 
# Create the CSV reader object
csv_reader = csv.reader(csv_file)
  
# Create the header object, advance the CSV reader to the header line by using the next() function
header = next(csv_reader)
   
# Search the headers for specifics strings and store
interface = header.index("interface")
description = header.index("description")
vlan = header.index("vlan")

class NetworkInterface(object):
    def __init__(self, name, description, vlan, uplink = True):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink

for row in csv_reader:
    interface_object = NetworkInterface(row[interface], row[description], row[vlan])
    print(template.render(intf=interface_object))
