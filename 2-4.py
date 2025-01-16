N = int(input())

# 상담기간과 수익을 저장할 리스트 초기화
sch = [list(map(int, input().split())) for _ in range(N)]

# 각 날짜부터 시작했을 때 얻을 수 있는 이익 저장
money = [0] * (N+1)

# 역순으로 최대 이익 계산(동적계획법이므로)
for i in range(N-1, -1, -1):
  time, profit = sch[i]
  if i + time <= N: # 상담할 수 있는 경우(상담을 선택한 경우)
    money[i] = max(profit + money[i+time], money[i+1]) 
  else: # 상담을 선택하지 않은 경우
    money[i] = money[i+1]

print(max(money))
