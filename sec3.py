# Strings & Lists

# Write a program to count vowels in a given string.
string=input("Enter a word: ")
vowels="aeiouAEIOU"
count=0
for i in range(len(string)):
  if string[i] in vowels:
    count+=1
print(count)

# Take a list of numbers and print the largest and smallest number.
numList=[1,2,3,4,5]
largest=numList[0]
smallest=numList[0]
for num in numList:
  if largest<num:
    largest=num
  if smallest>num:
    smallest=num
print(smallest, largest)

# Write a program to remove duplicates from a list.