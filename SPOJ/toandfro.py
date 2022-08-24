result = ""
while True:
  n = int(input())
  if n == 0:
    break
  en_msg = input()
  rows = len(en_msg)//n
  l = list()
  for i in range(rows):
    m = (i+1)*n
    if i%2 != 0:
      l.append(en_msg[i*n:m][::-1])
    else:
      l.append(en_msg[i*n:m])
  for j in range(n):
    for i in range(rows):
      result+=l[i][j]
  result+="\n"
print(result)

