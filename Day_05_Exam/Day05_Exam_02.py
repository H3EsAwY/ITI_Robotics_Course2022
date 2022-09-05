######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.05
# description:
#
# leap yeart problem
#
#
######################################################


def is_leap(year):
    leap = False
    
    if year%4==0:
        leap = True
    
    if year%100 == 0:
        leap = False
        
    if year%400 == 0:
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))
