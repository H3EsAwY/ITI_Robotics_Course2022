# Hany ALi ELesawy


num = int(input("Please Enter any number: "))

sum = 0
 
for x in range(1,num+1):
    sum = sum + x

avg = sum / num

print("The sum of natural numbers from 1 to" ,num, "=" ,sum,)

print("The average of natural numbers from 1 to" ,num, "=" ,avg,)
