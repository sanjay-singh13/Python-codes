t = int(input())

for i in range(t):
  l = list(map(int, input().split()))
  maxBorderLen = -1
  for it in range(l[0]): 
    count = 0
    consicutive = 1
    boundry = input()   
    if l[1]==1:
      if boundry[0]=="#":
        maxBorderLen = 1
      else:
        maxBorderLen = 0
    else:        
      for obj in range(l[1]):
        if boundry[obj] == "#":
          count = 1
          if obj > 0 and boundry[obj-1] == "#":
            consicutive = consicutive + count
        else:
          if consicutive > maxBorderLen:            
            maxBorderLen = consicutive
          consicutive = 1
          continue
  print(maxBorderLen)
    
