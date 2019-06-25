"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.

Also please include simple test function to test the class methods.
"""

class stringTest:
    value = ''
    def getString(self):
        self.value = input("Enter String")

    def printString(self):
        print(self.value.upper())

    def __init__(self,value):
        self.value = value
        print( "Constructor value : %s"  %self.value)


a = stringTest("HelloWorld")
a.getString()
a.printString()