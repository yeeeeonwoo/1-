# dfs는 재귀함수, stack으로 구현
def dfs(V):
  visited_dfs[V] = 1 # 시작점 방문처리
  print(V, end=' ') # 시작점 출력
  for i in range(1, N+1): # 번호가 1부터 시작하므로
    if(graph[V][i] == 1 and visited_dfs[i] == 0): # 시작점과 연결되어 있고 그 전에 방문한 적 없다면
      dfs(i) # 재귀함수 호출(한 시작점에 대해 모든 i가 돌아갈 때까지 기다리는게 아니라 바로 재귀함수 출력(깊이순))

def bfs(V): #bfs는 queue로 구현
  queue = [V] # 시작점 queue에 넣기
  visited_bfs[V] = 1 # 방문처리
  while queue: # queue가 비어있지 않다면
    V = queue.pop(0) # queue의 첫번째 원소 pop시키고 출력
    print(V, end = ' ')
    for i in range(1, N+1):
      if(graph[V][i] == 1 and visited_bfs[i] == 0):# 시작점과 연결되어 있고 그 전에 방문한 적 없다면
        queue.append(i) # queue에 넣기(한 시작점에 대해 모든 i를 queue에 넣기(너비순))
        visited_bfs[i] = 1

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)] # 각 정점마다 연결여부 저장하는 2차원 리스트(0: 연결안됨, 1: 연결됨)

for i in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1 # 연결되어 있다면 1로 바꾸기

# 방문한적 있는지 체크하는 용도
visited_dfs = [0] *(N+1)
visited_bfs = [0] *(N+1)

dfs(V)
print()
bfs(V)
