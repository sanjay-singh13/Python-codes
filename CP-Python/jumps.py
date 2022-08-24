def jumpingOnClouds(clouds):
  n = len(clouds)
  total_Jumps = 0
  hops = 0
  while hops < n:
    if hops + 2 <= n:
      if clouds[hops + 2] == 0:
        total_Jumps += 1
        hops += 2
      else:
        total_Jumps += 1
        hops += 1
  return total_Jumps

n = int(input())
clouds = list(map(int,input().split()))
print(jumpingOnClouds(clouds))