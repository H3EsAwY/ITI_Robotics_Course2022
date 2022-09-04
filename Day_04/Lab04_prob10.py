######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q10. Write to program to find the highest frequency element
######################################################


def getMostFreq(lstNum):
	
	currentFreq=0
	highestFreq=0
	mostFreqNum = lstNum[0]
	
	for num in lstNum:
		currentFreq = lstNum.count(num)
		
		if currentFreq>highestFreq :
			highestFreq = currentFreq
			mostFreqNum = num
			
	return num
	
	
#main

lstNum = input("Enter list of integers to find 2highest frequency element (Ex: 2 6 36): ").split()

print(f"The highest frequency element is: {getMostFreq(lstNum)}")
		
