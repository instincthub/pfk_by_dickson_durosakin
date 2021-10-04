#asking for user input and converting the input into integers
first_number = int(input("what is the first number? "))
second_number = int(input("what is the second number? "))

#performing calculation on the user input
addition = first_number + second_number
subtraction = first_number - second_number
division = round(first_number / second_number,2)
multiplication = first_number * second_number

#printing out the result into the console
print()
print("addition = "+str(addition))
print("subtraction = "+str(subtraction))
print("division = " + str(division))
print("multiplication = "+str(multiplication))
