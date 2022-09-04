######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q1. Write a program to check whether given number is prime or not.
######################################################


import math

num = int(input())
isPrime = True

# if the number is not divisible by any number from 2 to sqrt(num) then it is a prime

for i in range(2, round(math.sqrt(num) + 1) ):
	if num%i == 0:
		isPrime = False
		break
		
		
if isPrime == True:
	print(f"{num} is a Prime Number")
else:
	print(f"{num} is a NOT Prime Number")
		
