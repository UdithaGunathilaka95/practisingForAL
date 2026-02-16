# Functions

# Write a function that checks whether a string is a palindrome.
def isPalindrome(Str):
  revStr=""
  for i in range(len(Str)-1,-1,-1):
    revStr+=Str[i]
  return revStr==Str
  
print(isPalindrome("not"))

# Write a function that takes a list of numbers and returns a new list with only even numbers.
numList=[1,2,3,4,5]

def onlyEven(numList):
  resList=[]
  for num in numList:
    if num%2==0:
      resList.append(num)
  return resList

print(onlyEven(numList))
