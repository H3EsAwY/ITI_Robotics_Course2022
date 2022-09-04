######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q2. Write a program to print prime numbers in a given range. Ex: [5,70]
######################################################


import math

def isPrime(num):

	isPrimeFlag = True


	for i in range(2, round(math.sqrt(num) + 1) ):
		if num%i == 0:
			isPrimeFlag = False
			break
	
	return isPrimeFlag
	
	
#main

primeLst = [] 

numLst = input("Enter a range to check for prime numbers (Ex: 5,70) :  ").split(',')
numLst = list(map(int, numLst))

for i in range( numLst[0], numLst[1] + 1):

	if isPrime(i) == True:
		primeLst.append(i)
		

print(f"The Prime numbers between {numLst[0]} and {numLst[1]} are:")
print(primeLst)
