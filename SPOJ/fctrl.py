def Z(n):
  zeros = 0
  if n < 5:
    return 0
  while n>=5:
    zeros += n // 5
    n //= 5
  return zeros

t = int(input())
result = ""
while t > 0:
  t -= 1
  n = int(input())
  result += str(Z(n))+"\n"
print(result)