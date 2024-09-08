name = input("Please enter your name: ")
number = int(input((name) + ", please enter an integer: "))
number2 = int(input((name) + ", please enter another integer: "))
remainder = (number) % (number2)
if remainder == 0:
  print (str(number) + " is divisible by " + str(number2))
if remainder != 0:
  print (str(number) + " is NOT divisible by " + str(number2))