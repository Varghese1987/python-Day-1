#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lenovo
#
# Created:     31-03-2020
# Copyright:   (c) Lenovo 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass
    tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol','David'],
    ['dogs', 'cats', 'moose', 'goose']
    ]
    str1=""
    for x in range(4):
        for item in tableData:
            length = len(max(item,key=len))
            strlen = len(item[x])
            diff = length-strlen+1
            str1 += " "*diff+item[x]
        print(str1)
        str1=""
if __name__ == '__main__':
    main()
