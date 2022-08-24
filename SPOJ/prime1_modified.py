import math,time

def isPrime(n):
  if n == 1:
    return False
  elif n == 2 or n == 3:
    return True
  
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i+2) == 0:
      return False
    i += 6
  return True
t = int(input())

while t>0:
  out = ""
  m, n = map(int,input().split())
  start_time = time.time()
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
    if m!=23 and m%23==0:
      m+=2
      continue
    if m!=29 and m%29==0:
      m+=2
      continue
    if m!=31 and m%31==0:
      m+=2
      continue
    if m!=37 and m%37==0:
      m+=2
      continue
    if m!=41 and m%41==0:
      m+=2
      continue
    if m!=43 and m%43==0:
      m+=2
      continue
    if m!=47 and m%47==0:
      m+=2
      continue
    if isPrime(m):
      out += str(m)+"\n"
    m += 2
  print(out)
  t -= 1
print("-- %s seconds --" %(time.time()-start_time))