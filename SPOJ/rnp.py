
p = list("+-*/^")
op = list("abcdefghijklmnopqrstuvwxyz")

t = int(input())
result = ""
while t > 0:
  t -= 1
  infix = input()
  length = len(infix)
  stack = list()
  i = 0
  while i < length:
    x = infix[i]
    if x in op:
      result += x
    elif x in p:
      if len(stack)==0 or ('(' == stack[-1]) or p.index(x)>p.index(stack[-1]):
        stack.append(x)
      else:
        while p.index(stack[-1]) >= p.index(x):
          if stack[-1]!='(':
            result += stack.pop()
        stack.append(x)
    if x == '(':
      stack.append(x)
    
    if x == ')':
      while stack[-1] != '(':
        result += stack.pop()
      stack.pop()
    i += 1
  result += "\n"
print(result)
