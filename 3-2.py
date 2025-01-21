def dfs(node):
  visited[node] = True
  for i in range(1, N+1):
    if graph[node][i] == 1 and not visited[i]:
      dfs(i)

N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

# 그래프 입력받기
for i in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

visited = [False]*(N+1)
count = 0 # dfs 몇번했는지(dfs 횟수 = 연결요소 개수)
# 모든 정점에 대해서 방문한 적 없다면 dfs 수행
for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)

