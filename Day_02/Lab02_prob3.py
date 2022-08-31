# Hany ALi ELesawy

print("Enter 'q' for exit")

while(1):
    userInput = input("Enter any number: ")
    
    if userInput == 'q':
        break;
        
    num = int(userInput)
    
    if num%2 == 0:
      print(num, "is an even number")
    else:
      print(num, "is an odd number")
	
