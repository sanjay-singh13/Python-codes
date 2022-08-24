result = ""
while True:
  no_of_packets = int(input())
  store = list()
  if no_of_packets == -1:
    break
  sum_of_candies = 0
  counter = no_of_packets
  while counter>0:
    no_of_candies = int(input())
    store.append(no_of_candies)
    sum_of_candies += no_of_candies
    counter -= 1
  avg_of_candies = sum_of_candies//no_of_packets
  if sum_of_candies%no_of_packets != 0:
    result += str(-1)+"\n"
  else:
    moves = 0
    for x in store:
      if (avg_of_candies-x)>0:
        moves+=avg_of_candies-x
    result+=str(moves)+"\n"

print(result)
        