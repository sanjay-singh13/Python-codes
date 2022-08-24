import math

def reverseNum(n):
  rev = 0
  while n > 0:
    rev =10*rev + (n % 10)
    n //= 10
  return rev

t = int(input())
result = ""
while t>0:
  t-=1
  a, b = map(int,input().split())
  first = reverseNum(a)
  second = reverseNum(b)
  result+= str(reverseNum(first+second))+"\n"
print(result)
