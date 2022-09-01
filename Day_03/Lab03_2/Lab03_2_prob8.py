######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q8. 
######################################################

Sum = 0
numCounter = 0
avg = 0  
ipNum = None

while 1 :
	
	ipNum = int(input("Enter a number: ")) 
	
	if ipNum == 0:
		break
		
	Sum += ipNum
	numCounter += 1	
	
avg = Sum / numCounter

print(f"sum = {Sum}, Average = {avg}")
