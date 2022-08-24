
#For Connected Graphs
print("Enter the number of nodes in the graph:")
V = int(input())
visited = [0]*V
G = [[0]*V]*V
for i in range(V):
  print("Nodes adjacent to "+str(i))
  G[i] = list(map(int,input().split()))

def dfs(G,v):
  V = len(G)
  visited[v] = 1
  print(v,end=" ")
  while True:
    for w in range(V):
      if G[v][w] == 1 :
        if visited[w]==0:
          dfs(G,w)
    return


def main():
  dfs(G,0)




if __name__ == "__main__":
    main()