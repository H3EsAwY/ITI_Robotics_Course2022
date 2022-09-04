######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q7. Write a program to count the number of vowels in a given string.
######################################################


def countVowels(string):

	vowelCount = 0
	lstVowels = list("aeiou")
	
	string = string.lower()
	
	for letter in string:
		if letter in lstVowels:
			vowelCount += 1
			
	return vowelCount
	
	
#main

string = input("Enter a string to count its vowels: ")
print(f"The number of vowels is: {countVowels(string)}")
	


