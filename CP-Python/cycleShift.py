def binaryNum(bn):
  dn = 0
  for i in range(n):
    dn = dn + int(bn[n-i-1])*2**i
  return dn

def singleCycle(bn):
  nbn = ""
  fn, i = bn[0], 1
  while i < n:
    nbn = nbn + bn[i]
    i = i + 1
  nbn = nbn + fn
  return nbn

t = int(input())
for i in range(t):
  n, k = map(int,input().split())
  bn = input()
  adn = binaryNum(bn)
  maxdn = adn
  it, maxpos = 0,0
  bn = singleCycle(bn)
  while True:
    it = it + 1
    b = binaryNum(bn)
    if b > maxdn:
      maxdn = b
      maxpos = it
    if b == adn:
      break
    else:
      bn = singleCycle(bn)
  result = (k-1)*it + maxpos
  print(result)