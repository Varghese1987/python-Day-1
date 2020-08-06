#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     05-08-2020
# Copyright:   (c) Lenovo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
    input="XLI"
    roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100}
    i=0
    num=0
    while i<len(input):
        if i+1 < len(input) and input[i:i+2] in roman:
            num += roman[input[i:i+2]]
            i += 2
        else:
            num+=roman[input[i]]
            i += 1
    print(num)
if __name__ == '__main__':
    main()
