cost = [[0,10,30],[10,0,20],[30,20,0]]

t = [[0,0],[0,0]]
k = 0
l = 0
near = [0,0,0]
minCost = 10000007
for i in range(3):
    for j in range(3):
        c = cost[i][j]
        if c>0 and c<minCost:
            minCost = c
            k = i
            l = j


t[0][0] = k
t[0][1] = l

for i in range(3):
    if i==k or i==l:
        continue
    if cost[i][l]<cost[i][k]:
        near[i] = l
    else:
        near[i] = k

near[k] = 0
near[l] = 0

for i in range(1,2):
    for j in range(len(near)):
        if near[j]!=0:
            break
    minCost = minCost + cost[j][near[j]]
    t[i][0] = j
    t[i][1] = near[j]
    near[j] = 0
print(minCost)
print(t)
print(near)
        
