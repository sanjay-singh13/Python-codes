T = int(input())

for i in range(T):
  n, k = map(int,input().split())
  a = list(map(int,input().split()))
  r = k%n
  rotatedArray = []
  for i in range(n-r, n):
    print(a[i], end=" ")
  for i in range(0,n-r):
    print(a[i], end=" ")
  print("\n")
    



