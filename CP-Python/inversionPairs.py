t = int(input())
for it in range(t):
  n = int(input())
  M = []
  count = 0
  for i in range(n):
    M.append(list(map(int,input().split())))
  for i in range(n):
    for j in range(n):
      for p in range(n):
        for q in range(n):
          if i<=p and j<=q:
            if M[i][j] > M[p][q]:
              count = count + 1
              
  print(count)




