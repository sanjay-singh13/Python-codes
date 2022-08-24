def binaryNum(bn):
  dn = 0
  for i in range(n):
    dn = dn + int(bn[n-i-1])*2**i
  return dn

# def singleCycle(bn):
#   nbn = ""
#   fn, i = bn[0], 1
#   while i < n:
#     nbn = nbn + bn[i]
#     i = i + 1
#   nbn = nbn + fn
#   return nbn

n = int(input())
bn = input()
adn = binaryNum(bn)
maxdn = adn
it, maxpos = 0,0
leftRotation = ((adn << 1) | (adn >> (n - 1)))
print(adn, leftRotation)
# bn = singleCycle(bn)
# while True:
#   it = it + 1
#   # b = binaryNum(bn)
#   if leftRotation > maxdn:
#     maxdn = leftRotation
#     maxpos = it
#   if leftRotation == adn:
#     break
#   else:
#     leftRotation = (adn << 1) | (n >> (64 - 1))
# print(it,maxdn, maxpos)