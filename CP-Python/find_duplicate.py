

def find_dup(l):
  tortosie = 0
  hare = 0
  end = len(l)-1
  while tortosie!=end and hare!=end:
    tortosie += 1
    hare += 2
    if(l[tortosie] == l[hare%(end+1)]):
      tortosie = 0
      while l[tortosie] != l[hare]:
        tortosie += 1
        hare += 1
    print(l[hare%(end+1)])
    return

l = list(map(int,input().split()))

find_dup(l)