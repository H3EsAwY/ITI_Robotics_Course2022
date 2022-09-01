######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q10. 
######################################################


	
def getMaxMin(lstNum):
	Max = Min = lstNum[0]

	for i in lstNum:
		if i>Max:
			Max = i
		if i<Min:
			Min = i
			
	# or just use max() and min ()
	return Max, Min
	
lst=[100,30,22,40,60,20,10,300]
	

print(getMaxMin(lst))
	
