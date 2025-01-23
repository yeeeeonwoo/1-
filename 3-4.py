from collections import deque

def bfs(x, y):
  queue = deque([[x, y]])
  board[x][y] = 0
  num = 1

  while queue:
    x, y = queue.popleft()
    # 상하좌우에 인접한 집들이 있으면 큐에 넣고 0으로 처리
    # 상(x, y-1)
    if y-1 >= 0 and board[x][y-1] == 1:
      queue.append([x, y-1])
      board[x][y-1] = 0
      num += 1
    # 하(x, y+1)
    if y+1 < N and board[x][y+1] == 1:
      queue.append([x, y+1])
      board[x][y+1] = 0
      num += 1
    # 좌(x-1, y)
    if x-1 >= 0 and board[x-1][y] == 1:
      queue.append([x-1, y])
      board[x-1][y] = 0
      num += 1
    # 우(x+1, y)
    if x+1 < N and board[x+1][y] == 1:
      queue.append([x+1, y])
      board[x+1][y] = 0
      num += 1
  return num

N = int(input())
board = [list(map(int, input())) for _ in range(N)]

complex_sizes= []

for i in range(N):
  for j in range(N):
    if board[i][j] == 1:
      complex_sizes.append(bfs(i, j))

complex_sizes.sort()
print(len(complex_sizes))
for size in complex_sizes:
  print(size)
