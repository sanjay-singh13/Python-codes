# bucket = [2,1,1,1,2,1,1,2,1,2,1,1]
bucket = [0,1,2,1,0,0,2,1,0,2,1,0,0,1,1]

start, current, end = 0,0,len(bucket)-1
temp = -1
temp2 = -2

while current != end:
  if bucket[current] == 1:
    current = current + 1
  elif bucket[current] > 1:
    temp = bucket[current]
    bucket[current] = bucket[end]
    bucket[end] = temp
    end = end - 1
  else:
    temp2 = bucket[current]
    bucket[current] = bucket[start]
    bucket[start] = temp2
    start = start + 1
    current = current + 1
  

print(bucket)


# print("Number of Zero: ",zeros, "\nNumber of One: ",ones, "\nNumber of Two: ",twos)