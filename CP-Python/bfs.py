
#For Connected Graphs

from queue import Queue

def bfs(G,v):
  V = len(G)
  visited = [0]*V
  visited[v] = 1
  Q = Queue(V)
  u = v
  print(v,end=" ")
  while True:
    for w in range(V):
      if G[u][w] == 1 :
        if visited[w]==0:
          Q.put(w)
          visited[w] = 1
          print(w,end=" ")
    if Q.empty():
      return
    else:
      u = Q.get()


def main():
  print("Enter the number of nodes in the graph:")
  V = int(input())
  G = [[0]*V]*V
  for i in range(V):
    print("Nodes adjacent to "+str(i))
    G[i] = list(map(int,input().split()))
  bfs(G,0)




if __name__ == "__main__":
    main()