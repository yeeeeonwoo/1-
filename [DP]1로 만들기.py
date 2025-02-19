N = int(input())
# num[i]는 i를 1로 만드는데 필요한 최소 연산 횟수를 저장
num = [0]*1000001

for i in range(2, N+1):
  # 2로도 3으로도 나누어떨어지지 않을 때는 i-1로 이동하는데 1번 연산 수행했으니까 +1
  num[i] = num[i-1] + 1
  # 2로 나누어 떨어질 때는 i//2로 이동하는데 1번 연산 수행했으니까 +1(즉, i//2를 하는 것이 연산횟수가 적은지 안하는 것이 연산횟수가 적은지 비교)
  if(i%2 == 0):
    num[i] = min(num[i], num[i//2] + 1)
  # 3으로 나누어 떨어질 때 i//3으로 이동하는데 1번 연산 수행했으니까 +1(즉, i//3를 하는 것이 연산횟수가 적은지 안하는 것이 연산횟수가 적은지 비교)
  if(i%3 == 0):
    num[i] = min(num[i], num[i//3] + 1)

print(num[N])
