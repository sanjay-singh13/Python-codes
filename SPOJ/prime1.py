import math

def isPrime(n):
  if n==1:
    return False
  if n==2 or n==3:
    return True
  else:
    i = 2
    while i <= math.sqrt(n):
      if n % i == 0:
        return False
      i += 1
    return True



primes = list()
m, n = 1,100001
if m < 2:
  primes.append(2)
  m = 3
if m % 2 == 0:
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
    primes.append(m)
  m += 2


t = int(input())

while t>0:
  t-=1
  m, n = map(int,input().split())
  out = [x for x in range(m,n+1)]
  length = n-m+1
  i = 0
  while primes[i] <= math.sqrt(n):
    for x in range(length):
      if out[x]>primes[i] and out[x]%primes[i]==0:
        out[x] = 0
    i+=1
  result = ""
  for i in range(length):
    if out[i]!=1 and out[i]!=0:
      result+=str(out[i])+"\n"
  print(result)
  


      