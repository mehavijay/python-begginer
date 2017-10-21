#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16cse023
#
# Created:     20/10/2017
# Copyright:   (c) 16cse023 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
stringVar = "abcdefghijkxxxxxxxabcedf"
loc = stringVar.count('x') #counts the number of occurrences of 'x' in stringVar
print loc
loc = stringVar.find('x') # returns the position of character 'x'
print loc
stringVar = stringVar.lower() # returns the stringVar in lowercase (this is temporary)
print stringVar
stringVar = stringVar.upper() # returns the stringVar in uppercase(this is temporary)
print stringVar
stringVar = stringVar.replace('a', 'b') # replaces all occurrences of a with b in the string
print stringVar
stringVar = stringVar.strip() # removes leading/trailing white space from string
print stringVar