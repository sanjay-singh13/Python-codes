obj = [1,2,3,4,5,6]
profit = [3,1,13,15,5,12]

for j in range(1,6):
    key = obj[j]
    i = j-1
    while i>=0 and profit[obj[i]-1] < profit[key-1]:
        obj[i+1] = obj[i]
        i = i-1
    obj[i+1] = key
print(obj)

