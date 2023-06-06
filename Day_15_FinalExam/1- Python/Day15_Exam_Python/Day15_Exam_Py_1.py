###############################################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.21
#
# description:
# Read an array X[10]. After, replace every null or negative
# number of X ​by 1. Print all numbers stored in the array X.
#
###############################################################################


def replaceNeg (lst):

    lst_new = []
    for i in lst:
        if i <= 0:
            lst_new.append(1)
        elif i > 0:
            lst_new.append(i)

    return lst_new


def main():
    
    str_lst = input("Enter a list of number separated by spaces: ").split()
    
    replaceNeg_lst = replaceNeg(map(int, str_lst))

    for i in range(len(replaceNeg_lst)): 
        print(f"X[{i}] = {replaceNeg_lst[i]}")



main()