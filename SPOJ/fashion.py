t = int(input())
result = ""
while t>0:
  t-=1
  n = int(input())
  men = list(map(int,input().split()))
  women = list(map(int,input().split()))
  men.sort()
  women.sort()
  sum = 0
  for i in range(n):
    sum += men[i]*women[i]
  result += str(sum)+"\n"
print(result)