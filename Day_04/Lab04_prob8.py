######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q8. Write a program to get the second highest number in an array of integers.
######################################################

def get2ndHighest(lstNum):
	
	lstNum = list(set(lstNum))
	lstNum.sort()
	
	return lstNum[-2]
	
	
	
#main

lstNum = input("Enter array of integers to find 2nd highest (Ex: 2 6 36): ").split()

lstNum = list(map(int, lstNum))

print(f"The 2nd highest integer is: {get2ndHighest(lstNum)}")
