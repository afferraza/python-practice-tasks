"""
Write a Python program to find urls in a string and output all urls as list.
"""

import re

pattern = re.compile("https*://[\w.@_!#$%^&*()<>?/\|}{~:\w]*\S")

sample_data = "My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of http://www.geeksforgeeks.org"

print(re.findall(pattern,  sample_data))
