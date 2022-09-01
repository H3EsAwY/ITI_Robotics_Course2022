######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q4. check a character is vowel or not.
######################################################

vowels = ['a', 'e', 'i', 'o', 'u']


isVowel = False

ipChar = input("Enter a character to check if it is a vowel or not: ")

for x in vowels:
	if ipChar==x:
		isVowel = True
		break

		
if isVowel==True:
	print("The character is a vowel")
else:
	print("The character is NOT vowel")
