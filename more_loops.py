number = int(input("Please enter a number from 1-100: "))
while number < 1 or number > 100:
  print("Invalid number.")
  number = int(input("Please enter a number from 1-100:"))
print("Thank you for your input. ")

variable = 1
color = input("What do you think my favourite color is?: ")
while color != "pink":
  print("That is incorrect.")
  color = input ("What do you think my favourite color is: ")
  variable = variable + 1
print("You are correct it took you " + str(variable) + " attempts.")

total = 0
amount = int(input("How many numbers would you like to add? "))
for i in range(amount):
  num = int(input("Please enter a number: "))
  total = total + num
print( "Your sum is: " + str(total))