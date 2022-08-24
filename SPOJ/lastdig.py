t = int(input())
result = ""
while t>0:
  t-=1
  a, b = map(int,input().split())
  ld = a%10
  if b==0:
    result += str(1)+"\n"
  elif ld==0 or ld==1 or ld==5 or ld==6:
    result += str(ld)+"\n"
  else:
    if b%4 == 0:
      result += str((ld**4)%10)+"\n"
    else:
      result += str((ld**(b%4))%10)+"\n"
print(result)