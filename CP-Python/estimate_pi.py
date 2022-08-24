import random, math

def estimate_pi(n):
  points_inside_circle = 0
  points_outside_circle = 0
  for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    d = math.sqrt(x*x + y*y)
    if d<=1:
      points_inside_circle += 1
    points_outside_circle += 1
  print(4*points_inside_circle/points_outside_circle)

estimate_pi(int(input()))