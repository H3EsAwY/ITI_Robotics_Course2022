######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q6. Write a program to remove given character from a string. Ex: ‘c’
######################################################



def removeChar(string, char):
	
	newString = string.replace(char,'')
	
	return newString
	
	
	
	
	
#main

string = input("Enter a string: ")
char =   input("Enter a char to remove: ")

print(f"The string after removing '{char}' is: {removeChar(string, char)}")




