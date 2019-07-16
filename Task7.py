"""
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
Bag,hello,without,world

"""

import re

pattern = re.compile("\w*[^,]")
sample_data = "without,hello,bag,world"

words = re.findall(pattern,  sample_data)
words.sort()
seperator = ','
print(seperator.join(words))
