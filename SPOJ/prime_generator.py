import math
def isPrime(n):
  if n==1:
    return False
  if n==2 or n==3:
    return True
  else:
    if n % 2 == 0:
      return False
    i = 3
    while i <= math.sqrt(n):
      if n % i == 0:
        return False
      i += 2
    return True


t = int(input())

while t>0:
  out = ""
  m, n = map(int,input().split())
  if m <= 2:
    out+=str(2)+","
    m = 3
  if m!=2 and m % 2 == 0:
    m += 1
  while m <= n:
    if m!=3 and m%3==0:
      m+=2
      continue
    if m!=5 and m%5==0:
      m+=2
      continue
    if m!=7 and m%7==0:
      m+=2
      continue
    if m!=11 and m%11==0:
      m+=2
      continue
    if m!=13 and m%13==0:
      m+=2
      continue
    if m!=17 and m%17==0:
      m+=2
      continue
    if m!=19 and m%19==0:
      m+=2
      continue
    if isPrime(m):
      out += str(m)+","
    m += 2
  print(out)
  t -= 1


    