######################################################
# Name:  Hany Ali Elesawy
# Date:  2022.09.01
# Topic: Lab03_2 Q3. accept number from 1 to 7 and display name of day
######################################################

weekDays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

dayNum = int(input("Please enter a number of day from 1 to 7: "))

print(f"Name of day {dayNum}: {weekDays[dayNum-1]} ")
