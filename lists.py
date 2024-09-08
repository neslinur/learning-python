#Neslinur Kaya
#January 18, 2022
#4.5 Exercise lists

names = ["Peter", "Bruce", "Steve", "Tony", "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol" ]
numbers = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]


#program 1
#A loop that will output every other name in the names list.

for name in names: 
  if names.index(name) % 2 == 1 : 
    print(name)
print()
#program 2
#A loop that will output only the positive numbers in the numbers list.

temp_list_pos = []

for i in numbers:
  if 0 < i:
    temp_list_pos.append(i)

print("Positive numbers in the list are: " + str(temp_list_pos))


#program 3
#A loop that will output the sum of all the values in the numbers list.
total = 0
for i in numbers:
 total = total + i

print("The sum of all numbers in the list is: " + str(total))

#program 4
#A loop that will output only the numbers that are odd.
temp_list_odd = []
for i in numbers:
  if i % 2 != 0:
    temp_list_odd.append(i)

print("The odd numbers in the list are: " + str(temp_list_odd))
#program 5
#A loop that will output only the names that come before "Thor" in the alphabet from the names list.
namesthor = names
namesthor.sort()
namesthor.reverse()
for x in namesthor:
  for y in x:
    if "T" in y or "W" in y:
      namesthor.remove(x)

print(namesthor)
  
#program 6
#A loop that will  find the maximum or minimum value in the numbers list.
print("The largest number in the list is: " + str(max(numbers)))
print("The smallest number in the list is: " + str(min(numbers)))