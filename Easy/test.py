import xml.etree.ElementTree as ET
from collections import defaultdict

# Pass the path of the xml document
tree = ET.parse('items.xml')

# get the parent tag
root = tree.getroot()

mdExch_dict = defaultdict(int)
for index, value in enumerate(root.findall('.//mdExch')):
    mdExch_dict[value.text] += 1

duplicates = [word for word, occurrences in mdExch_dict.items() if occurrences > 1]
print(duplicates)