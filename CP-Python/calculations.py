# def Tn(n):
#   if n == 1:
#     return 3
#   elif n == 2:
#     return 2
#   elif n == 3:
#     return 1
#   else:
#     return Tn(n-1) + Tn(n-2) + Tn(n-3)

Tn = [0]*1000000000000000000
Tn[1] = 3
Tn[2] = 2
Tn[3] = 1


S = 0
M = 1000000007
N = int(input())
for i in range(N):
  S = S + Tn(i+1)*Tn(i+1)
print(S%M)
