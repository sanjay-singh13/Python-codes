import sys
val = [0]*100001
for i in range(100001):
  if i < 12:
    val[i] = i
  else:
    val[i] = val[i//2] + val[i//3] + val[i//4]

def fun(n):
  if n<=100000:
    return val[n]
  return (fun(n//2)+fun(n//3)+fun(n//4))

for line in sys.stdin:
  for var in line.split():
    var = int(var)
    print(fun(var))

  