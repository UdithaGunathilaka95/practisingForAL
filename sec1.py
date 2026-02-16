# Basics
# Write a Python program that takes an integer input from the user and prints whether it is even or odd.
num=int(input("Enter a number: "))
if num%2==0:
  print("Even")
else:
  print("Odd")

# Write a Python program to calculate the sum of all numbers from 1 to N, where N is user input.
endNum=int(input("Enter a number: "))
tot=0
for i in range(1, endNum+1):
  tot+=i
print(tot)

# Write a program that converts Celsius to Fahrenheit. (Formula: F = C × 9/5 + 32)
cel=int(input("Enter celsious value: "))
celToFah=cel*9/5+32
print(celToFah)