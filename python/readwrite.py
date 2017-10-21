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

 file = open("testfile.txt","w")

 file.write("Welcome Guvi........")

 file.close()
file = open("testfile.txt", "r")
print file.read()

if __name__ == '__main__':
    main()
