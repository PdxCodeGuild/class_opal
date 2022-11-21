import re
from pprint import pprint


test_string = """
Mr. John Smith: 123-456-7890
Mrs. Jane Smith: 234---567-8901
Jack Smith: +1 345-678-9012
Jenny Smith: 456.789.....0123
Bob Smith: +9845 567-890-1234
Smith
Sophie Smithberg: 1 6789012345
George Greensmith: +1 (789) 012-3456
Peter Parker: 1 (890)123-4567
123-12-1234
"""

# r'' defines a raw string
names_expression = r'([A-Za-z]*)\s*(\w*[Ss]mith\w*)'
smiths = re.findall(names_expression, test_string)

# Expressions that include one or more capturing groups will return a list of tuples
# Tuples include one value for the output of each capturing groups
print(smiths)


numbers_expression = r'(\d{0,4}\s?)(\(?\d{3}\)?\s?[-\.]?\d{3}[-\.]?\d{4})'
phone_numbers = re.findall(numbers_expression, test_string)
print(phone_numbers)


big_expression = r'(([A-Za-z]*)\s*(\w*[Ss]mith\w*)):\s\+?((\d{0,4}\s?)(\(?\d{3}\)?\s?[-\.]?\d{3}[-\.]?\d{4}))'

# When there are nested capturing groups,
# you will get the output of the WHOLE group AND the sub-groups
# in the order that the groups are defined in
address_book = re.findall(big_expression, test_string)
pprint(address_book)
