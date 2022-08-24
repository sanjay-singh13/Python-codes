print("Enter Number of Objects and Capacity of Knapsack")
n, m = map(int,input().split())



print("Enter Weight Array of Objects")

weight = list(map(int,input().split()))

print("Enter Profit Array of Objects")

profit = list(map(int,input().split()))

P = 0

pbyw = list()
obj = list()
for i in range(n):
    obj.append(i+1)
    pbyw.append(profit[i]/weight[i])


for j in range(1,n):
    key = obj[j]
    i = j-1
    while i>=0 and pbyw[obj[i]-1] < pbyw[key-1]:
        obj[i+1] = obj[i]
        i = i-1
    obj[i+1] = key

for i in range(n):
    if m>0 and weight[obj[i]-1]<=m:
        m = m-weight[obj[i]-1]
        P = P + profit[obj[i]-1]
    else:
        break

print(i)
if m>0:
    P = P + profit[obj[i]-1]*(m/weight[obj[i]-1])

print(P)

