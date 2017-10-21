#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      16ece002
#
# Created:     20/10/2017
# Copyright:   (c) 16ece002 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
list = ['ranju', 'subu', 'bagss', 'myth', 'nisanth']
def foo(x):
     print x * 5


def my_map_simple(fun, list):
     for item in list:
         fun(item)


my_map_simple(foo, list)

