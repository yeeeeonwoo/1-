N=int(input()) # 계단 개수
stairs=[int(input()) for _ in range(N)] # 계단 리스트
dp=[0]*(N) # dp 리스트
if len(stairs)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(stairs))
else: # 계단이 3개 이상일 때
    dp[0]=stairs[0] # 첫째 계단 직접 계산
    dp[1]=stairs[0]+stairs[1] # 둘째 계단까지 직접 계산
    for i in range(2,N): # 3번째 계단 부터 점화식 이용해서 최댓값 구하기
        dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i]) # 1계단 오르고 2번째 계단 건너뛰고 3번째 계단 오르기 vs 2계단 한번에 오르기
    print(dp[-1])
