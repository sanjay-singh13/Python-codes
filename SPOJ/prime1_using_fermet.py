import math, random
def gcd(a,b):
  if a < b:
    return gcd(b,a)
  elif a % b == 0:
    return b
  else:
    return gcd(b,a%b)

def isPrime(n,k):
  if n <= 1 or n == 4:
    return False
  if n <= 3:
    return True
  
  while k > 0:
    a = math.floor(random.uniform(2,n-1))

    if gcd(n,a) != 1:
      return False
    
    if math.pow(a,n-1)%n != 1:
      return False
    k -= 1
  return True



t = int(input())

while t>0:
  out = ""
  m, n = map(int,input().split())
  if m <= 2:
    out+=str(2)+"\n"
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
    if isPrime(m,20):
      out += str(m)+"\n"
    m += 2
  print(out)
  t -= 1

