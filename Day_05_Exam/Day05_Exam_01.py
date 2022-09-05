######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.05
# description:
#
# Write a function that takes a list of various data types and returns a dictionary with data
# types as keys and with the data in the input list as items. Note: Function type() returns
# data #type of input, example: type(3) will return intSample input
#
######################################################


def getDataTypeLst(lstInput):
	
	DictDataType = {}
	
	for item in lstInput:
		
		if type(item) not in DictDataType:
			DictDataType[type(item)] = [item]
		else:
			DictDataType[type(item)].append(item)
		
	return DictDataType			
	
	
# main

lstInput = [1, 1.3, 7, 4.4, 'hi', [0,1], '45']

print(getDataTypeLst(lstInput))



