###############################################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.21
#
# description:
# 
# In this problem you need to read 15 numbers and must put them into two different
# arrays: par if the number is even or impar if this number is odd. But  the size
# of each of the two arrrays is only 5 positions. So every time you fill one of two
# arrays, you must print the entire array to be able to use it again for the next
# numbers that are read. At the end, all remaining numbers of each one of these two 
# arrays must be printed beginning with the odd array. Each array can be filled how
# many times are necessary.
#
#
# So:
# 
# if even --> par
# if odd  --> impar
#
# if array is full print it then clear it
# 
# when you are done if there are any number left in the 2 lists print impar then par
#
###############################################################################


def main():
    
    str_lst = input("Enter a list of number separated by spaces: ").split()
    int_lst = map(int, str_lst)

    par = []
    impar = []

    for num in int_lst:

        if num%2 == 0:
            par.append(num)
        elif num%2 !=0:
            impar.append(num)
            

        if len(par) == 5:
            
            for i in range(len(par)):
                print(f"par[{i}] = {par[i]}")

            par.clear()


        if len(impar) == 5:
            
            for i in range(len(impar)):
                print(f"impar[{i}] = {impar[i]}")

            impar.clear()
        
    
    # At the end, all remaining numbers of each one of these two arrays
    # must be printed beginning with the odd array
    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}") 

    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")

    
main()