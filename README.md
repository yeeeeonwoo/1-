from itertools import product
N = input()
N = int(N)
Ncopy = N
M = 0
cnt = 0
min = 10000000000

while(Ncopy>0):
  Ncopy = Ncopy//10
  cnt = cnt+1

digits = [range(0,10)] * cnt

for combination in product(*digits):
  M = sum(combination) + sum(combination[i]*(10**(cnt-1-i)) for i in range(cnt))

  if(N == M):
    num = sum(combination[i]*(10**(cnt-1-i)) for i in range(cnt))
    if num < min:
      min = num

print(min)
