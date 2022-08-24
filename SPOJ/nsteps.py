t = int(input())
result = ""
while t>0:
  t-=1
  x, y = map(int,input().split())
  if y>=(x+1) or y==(x-1) or y<=(x-3):
    result+="No Number \n"
  else:
    if x%2==0 and y%2==0:
      result+=str(x+y)+"\n"
    else:
      result+=str(x+y-1)+"\n"
print(result)
