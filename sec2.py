# Loops & Conditionals

# Create a program that prints a multiplication table of a number entered by the user.
num=int(input("Enter a number: "))
for i in range(1,11):
  print(num*i, end=" ")

# Write a program to reverse a number entered by the user.
num=int(input("Enter a number: "))
strNum=str(num)
res=""
for i in range(len(strNum)-1,-1,-1):
  res+=strNum[i]
print(res)