from collections import deque

def bfs():
  queue = deque() 
  queue.append(n) # n부터 deque에 넣기

  while queue:
    x = queue.popleft()
    if x == k: # x가 k랑 같아지면 바로 몇초인지 출력
      print(distance[x])
      break
    for nx in (x-1, x+1, x*2):
      if 0 <= nx <= 100000 and not distance[nx]:
        distance[nx] = distance[x] + 1
        queue.append(nx)

distance = [0] * 100001
n, k = map(int, input().split())
bfs()
