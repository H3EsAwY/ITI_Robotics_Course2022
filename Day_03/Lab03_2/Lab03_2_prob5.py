######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q5. 
######################################################


markedPrice = int(input("Enter marked price: "))

if markedPrice>10000:
	discount = 0.2
	
elif markedPrice>7000 and markedPrice<=10000:
	discount = 0.15
	
elif markedPrice<=7000:
	discount = 0.10
	
net = markedPrice - discount*markedPrice

print(f"The net amount is: {net}")




