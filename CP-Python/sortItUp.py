bucket = [2,1,1,1,2,1,1,2,1,2,1,1]

zeros, ones, twos = 0,0,0

for i in range(len(bucket)):
  if bucket[i] == 0:
    zeros = zeros + 1
  elif bucket[i] == 1:
    ones = ones + 1
  else:
    twos = twos + 1

for i in range(zeros):
  bucket[i] = 0

for i in range(zeros, zeros+ones):
  bucket[i] = 1

for i in range(zeros+ones, zeros+ones+twos):
  bucket[i] = 2

print(bucket)


# print("Number of Zero: ",zeros, "\nNumber of One: ",ones, "\nNumber of Two: ",twos)