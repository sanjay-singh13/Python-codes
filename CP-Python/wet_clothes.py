def find_min(l):
  minVal = 100000007
  length = len(l)
  for i in range(length):
    if l[i]>0 and l[i]<minVal:
      minVal = l[i]
  return minVal

n, m, g = map(int,input().split())
rt_instant = list(map(int,input().split()))
d_cloth = list(map(int,input().split()))

ini_time = 0
maxClothes = 0
for i in range(n):
  val = find_min(d_cloth)
  opt_time = rt_instant[i]-ini_time
  if (opt_time) >= val:
    g-=1
    for j in range(m):
      if d_cloth[j]<=opt_time:
        maxClothes+=1
        d_cloth[j] = -1
  ini_time = rt_instant[i]
  if g == 0:
    break

print(maxClothes)
        