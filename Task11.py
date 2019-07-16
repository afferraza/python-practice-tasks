"""
Write a Python program to remove the parenthesis area in a string.

Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

"""

import re

pattern = re.compile("\([^()]*\)")
sample_data = ["example (.com)", "w3resource",
               "github (.com)", "stackoverflow (.com)"]
for data in sample_data:
    print(re.sub(pattern, '', data))
