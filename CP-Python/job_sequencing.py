print("Enter Number of Jobs")
n = int(input())

Jobs = list()
for i in range(n):
    Jobs.append(i+1)

print("Enter Deadlines of each job")
deadline = list(map(int,input().split()))

print("Enter Profit of each job")
profit = list(map(int,input().split()))


for j in range(1,n):
    key = Jobs[j]
    i = j-1
    while i>=0 and profit[Jobs[i]-1] < profit[key-1]:
        Jobs[i+1] = Jobs[i]
        i = i-1
    Jobs[i+1] = key

maxDeadline = -1
for i in range(n):
    if maxDeadline < deadline[i]:
        maxDeadline = deadline[i]

order = list()
for i in range(maxDeadline):
    order.append(0)


Total_Profit = 0

for i in range(maxDeadline):
    k = maxDeadline-1
    while k>=0:
        if k+1<=deadline[Jobs[i]-1] and order[k]==0:
            order[k] = Jobs[i]
            Total_Profit = Total_Profit + profit[Jobs[i]-1]
            break
        k = k-1


print("Sequence of Jobs")
for i in range(maxDeadline):
    if i != maxDeadline -1:
        print("Job"+str(order[i])+" -->",end=" ")
    else:
        print("Job"+str(order[i]),end=" ")

print("\nTotal Profit: "+str(Total_Profit))


        
        
