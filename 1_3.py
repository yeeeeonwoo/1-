# -*- coding: utf-8 -*-
"""1-3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DJm8X0TjmVci51IPdnm3uXbdZHnLul1h
"""

from concurrent.futures.thread import ThreadPoolExecutor
num = [] # 입력된 자연수들 저장

tri = [0] # 1000 근처의 삼각수 모음(tri[0] = 0 은 제외), i가 44일 때 990, i가 45일 때 1035
for i in range(1, 46):
  tri.append(int(i*(i+1)/2))

# T개의 자연수 입력받기
T = int(input())
for i in range(T):
  num.append(int(input()))

for a in range(T):
  K = num[a]
  Three = False # 정확히 3개의 삼각수로 표현되는지 아닌지 체크하는 플래그
  for b in range(1, 46):
    if num[a] < tri[b]:
      index = b - 1 # index는 입력된 자연수보다 같거나 작은 최대의 삼각수의 index를 저장함1
      break

  for i in range(1, index + 1):
    for j in range(1, index + 1):
      for k in range(1, index + 1):
        if tri[i] + tri[j] + tri[k] == K: # index 보다 작은 세 삼각수의 합이 K가 되면 True
          Three = True
          break

      if Three:
        break
    if Three:
      break


  if Three == True:
    print("1")
  else:
    print("0")