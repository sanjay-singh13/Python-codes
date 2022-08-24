fact = [0]*100
fact[0] = 1
for i in range(1,100):
  fact[i] = (i+1)*fact[i-1]

t = int(input())
result = ""
while t > 0:
  t -= 1
  n = int(input())
  result += str(fact[n-1])+"\n"
print(result)