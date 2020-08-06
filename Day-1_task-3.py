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
    input = 1
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if input > 12 or input < 1:
        print("Error")
    else:
        print(days[input])
if __name__ == '__main__':
    main()
