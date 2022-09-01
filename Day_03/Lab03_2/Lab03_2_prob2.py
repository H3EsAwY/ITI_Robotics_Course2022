######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q2. check if last digit of number is divisible by 3 or not
######################################################


num = int(input("Enter a number to check if its last digit is divisible by 3: "))

lastDig = num%10

if(lastDig%3 == 0):
	print(f"The number {lastDig} is divisible by 3")
else:
	print(f"The number {lastDig} is NOT divisible by 3")
