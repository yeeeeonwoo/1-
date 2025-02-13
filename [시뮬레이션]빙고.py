# 가로줄 빙고 확인 함수
def horizontal(board):
  count = 0
  for i in range(5):
    if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == 0:
      count += 1
  return count

# 세로줄 빙고 확인 함수
def vertical(board):
  count = 0
  for i in range(5):
    if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == 0:
      count += 1
  return count

# 대각선 빙고 확인 함수
def diagonal(board):
  count = 0
  if board[0][0] == board [1][1] == board[2][2] == board[3][3] == board[4][4] == 0:
    count += 1
  if board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0] == 0:
    count += 1
  return count

# 총 몇빙고인지 출력하는 함수
def bingo(board): 
  return horizontal(board) + vertical(board) + diagonal(board)

# 빙고 보드판
board = [list(map(int, input().split())) for _ in range(5)]

# 사회자가 부르는 숫자
answer = [list(map(int, input().split())) for _ in range(5)]

call_count = 0 # 사회자가 몇 번째 숫자를 불렀는지
bingo_found = False # 3빙고인지 아닌지 체크


for number_row in answer: # 사회가자 부르는 숫자들의 모든 라인에서
    for called_number in number_row: # 라인 안에 있는 모든 숫자를 하나씩 체크
      call_count += 1 # 숫자 하나 체크될 때마다 카운트 증가
      for i in range(0, 5):
        for j in range(0, 5):
          if board[i][j] == called_number: # 빙고판 숫자와 불린 숫자와 같으면 0으로 바꿈
            board[i][j] = 0
      if bingo(board) >= 3: # 모든 숫자마다 빙고인지 체크해야함
        print(call_count)
        bingo_found = True
        break
    if bingo_found:
      break
