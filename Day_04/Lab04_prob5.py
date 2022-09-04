######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q5. Write a program to check whether a number is binary or not.
######################################################


def isBinary(strNum):
	
	isBinaryNum = True
	
	for strDigit in strNum:
	
		if (strDigit != '0') and (strDigit != '1'):
				isBinaryNum = False
				break
				
	return isBinaryNum
	
#main

strNum = input("Enter a number to check if it's in binary format: ")

if isBinary(strNum) == True:
	print(f"{strNum} is in binary format")
else:
	print(f"{strNum} is NOT in binary format")
	
