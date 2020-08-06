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
    def listToStr(list):
        str1=""
        for item in list:
            if item == list[len(list)-1]:
                str1 += "and "+item
            elif item == list[len(list)-2]:
                str1 += item+" "
            else:
                str1 += item+", "
        return str1

    food = ['apples', 'bananas', 'tofu', 'soya']
    print(listToStr(food))

if __name__ == '__main__':
    main()
