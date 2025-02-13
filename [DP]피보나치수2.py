# tabulation 방식
def fibo(N, num):
  for i in range(2, N+1):
    num[i] = num[i-1] + num[i-2] # 점화식 세우기
  print(num[N])

# N 입력받기
N = int(input())
# num은 0으로 다 초기화
num = list([0]*100)
num[0] = 0
num[1] = 1

fibo(N, num)
