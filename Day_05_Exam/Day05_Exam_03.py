######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.05
#
# description:
# Write a credit card (CC) validation script
#
######################################################


def isValidCC(strCC):
	
	lstCreditCard = strCC.split('-')
	
	strStrippedCC = ''.join(lstCreditCard)
	
	creditState = True
	
	ccStartNum = strStrippedCC[0]
	
	if strCC.count("-") != 3:
		creditState = False
		return ( creditState ) 
		
	if len(strStrippedCC) != 16 :
		creditState = False
		return ( creditState ) 
		
	if ccStartNum != '4' and ccStartNum !='5' and ccStartNum !='6':
		creditState = False
		return ( creditState ) 
		
	for strNum in strStrippedCC:
		if strNum not in list("123456789"):
			creditState = False
			return ( creditState ) 
	

	for strNum in strStrippedCC:
		if strNum*4 in strStrippedCC:
			creditState = False
			return ( creditState ) 
		
	return creditState



#main

strCC = "5122-2368-7954-3214"
print(isValidCC(strCC))
