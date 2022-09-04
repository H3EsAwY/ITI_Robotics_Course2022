######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.04
# Topic: Lab04 Q9. Write a program to get unique characters in a string.
######################################################

def getUniqueChar(string):
	
	#removing all spaces from the string
	string = string.replace(' ', '')
	
	lstUnique = sorted(set(string))
	#sorted returns a sorted list of the set 
	#The returned list is sorted alphabetically 
	
	return lstUnique
	
	
#main


string = input("Enter a string to return all of the unique characters: ")
print(getUniqueChar(string))


