# Functions

# Write a function that checks whether a string is a palindrome.
def isPalindrome(Str):
  revStr=""
  for i in range(len(Str)-1,-1,-1):
    revStr+=Str[i]
  return revStr==Str
  
print(isPalindrome("not"))

# Write a function that takes a list of numbers and returns a new list with only even numbers.
def onlyEven(numList):
  resList=[]
  for num in numList:
    if num%2==0:
      resList.append(num)
  return resList

numList=[1,2,3,4,5]
print(onlyEven(numList))


def toBinary(num):
  binary=""
  res=""
  while num > 0:
    if num%2==0:
      binary+="0"
    else:
      binary+="1"
    num=num//2
  for i in range(len(binary)-1,-1,-1):
    res+=binary[i]
  return res

print(toBinary(128))

  



