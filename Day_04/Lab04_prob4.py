######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q4. Write a program to calculate the power without using POW function (using a for loop).
######################################################

def getPower(num, power):
	
	result = 1
	
	for i in range(power):
		result = result * num
		
	return result
	
	
	
#main

number = float(input("Enter number: "))
power = int(input("Enter power: "))

print(f"{number} raised to the power of {power} is: {getPower(number, power)}")
