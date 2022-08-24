n = int(input())
i = 1
sum = 0
while i*i <= n:
  sum += n//i - i + 1
  i += 1
print(sum)