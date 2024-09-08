#Neslinur Kaya
#1/25/2022
#4.6 Exercise B

import random

def check():
  if guess[0] == answer[0]:
    print("The first number is correct!")
  if guess[1] == answer[1]:
    print("The second number is correct!")
  if guess[2] == answer[2]:
    print("The third number is correct!")
  if guess[3] == answer[3]:
    print("The fourth number is correct!")

answer = []
for x in range(4):
  answer.append(random.randint(1,9))

guess = []

attempts = 0

while guess != answer:
  guess = []
  x = input("What is the first digit? ")
  guess.insert(0,int(x))
  x = input("What is the second digit? ")
  guess.insert(1,int(x))
  x = input("What is the third digit? ")
  guess.insert(2,int(x))
  x = input("What is the fourth digit? ")
  guess.insert(3,int(x))
  print(guess)
  check()

  attempts = attempts + 1

  if guess[0] == answer[0] and guess[1] == answer[1] and guess[2] == answer[2] and guess[3] == answer[3]:
    print("You have guessed the code!")
    print("It took you " + str(attempts) + " attempts!")