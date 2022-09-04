######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q3. Write a program to calculate average value of a given list.
######################################################


def getListAvg(lst):

	lstAvg = sum(lst) / len(lst)
	
	return lstAvg



# main

numLst = input("Enter a list to find its average (Ex: 2,3,6) : ").split(',')
numLst = list(map(int, numLst))

print(f"The list average is {getListAvg(numLst)}")
