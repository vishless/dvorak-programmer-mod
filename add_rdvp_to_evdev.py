# Python code to add the keyboard variant to evdev.xml

import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('/usr/share/X11/xkb/rules/evdev.xml')
root = tree.getroot()

# Locate the variantList element (assuming it's under the 'layout' element)
variant_list = root.find(".//variantList")

# Create the new variant entry
new_variant = ET.Element('variant')

config_item = ET.SubElement(new_variant, 'configItem')
name = ET.SubElement(config_item, 'name')
name.text = 'rdvp'

description = ET.SubElement(config_item, 'description')
description.text = 'English (Real Programmers Dvorak)'

vendor = ET.SubElement(config_item, 'vendor')
vendor.text = 'MichaelPaulson'

# Add the new variant entry to the variantList
variant_list.append(new_variant)

# Save the modified XML file
tree.write('/usr/share/X11/xkb/rules/evdev.xml')
