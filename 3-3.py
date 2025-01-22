from collections import deque

def bfs(x, y):
  queue = deque([[x,y]])
  board[x][y] = 0
  while queue:
    x, y = queue.popleft()
    # 상하좌우에 인접한 배추가 있으면 큐에 넣고 0으로 바꿔주기
    # 상(x, y-1)
    if y-1 >= 0 and board[x][y-1] == 1:
      queue.append([x, y-1])
      board[x][y-1] = 0
    # 하(x, y+1)
    if y+1 < N and board[x][y+1] == 1:
      queue.append([x, y+1])
      board[x][y+1] = 0
    # 좌(x-1, y)
    if x-1 >= 0 and board[x-1][y] == 1:
      queue.append([x-1, y])
      board[x-1][y] = 0
     # 우(x+1, y)
    if x+1 < M and board[x+1][y] == 1:
      queue.append([x+1, y])
      board[x+1][y] = 0

T = int(input())
for _ in range(T):
  M, N, K = map(int, input().split())
  # 배추밭 배열 다 0으로 초기화
  board = [[0] * N for _ in range(M)]
  # 배추가 있는 곳은 1로 표시
  for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 1
  # bfs 수행 횟수를 저장하는 변수 cnt
  cnt = 0
  for i in range(M):
    for j in range(N):
      if board[i][j] == 1:
        bfs(i, j)
        cnt += 1
  print(cnt)
