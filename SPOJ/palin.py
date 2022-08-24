t = int(input())

while t>0:
  t-=1
  dig = input()
  res = list(dig)
  size = len(dig)
  if size % 2 == 0:
    print("even")
  else:
    m_index = size // 2
    i = 1
    while i <= m_index:
      if m_index-i == m_index+i:
        print("hello")


