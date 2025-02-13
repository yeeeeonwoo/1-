import math
from itertools import permutations

# 사칙연산하는 함수
def calculations(number1, operator, number2):
  if operator == '+':
    return number1 + number2
  elif operator == '-':
    return number1 - number2
  elif operator == '*':
    return number1 * number2
  elif operator == '//':
    if(number1 < 0 and number2 > 0):
      number1 = abs(number1)
      return (-1) * (number1 // number2)
    else:
      return number1 // number2

# 최댓값, 최솟값 찾는 함수
def find_max_min(N, numbers, operator_counts):
  # operator_counts에 따라 연산자들로 구성된 operators 리스트 만들기
  operators =[] 
  operators.extend(['+'] * operator_counts[0])
  operators.extend(['-'] * operator_counts[1])
  operators.extend(['*'] * operator_counts[2])
  operators.extend(['//'] * operator_counts[3])
  
  max_value = float('-inf')
  min_value = float('inf')

  # N-1(연산자개수)개의 모든 순열
  for perm in permutations(operators, N-1):
    result = numbers[0]
    for i in range(1, N): # 모든 연산자의 경우의 수에 대해서 계산하고 최댓값, 최솟값 저장
      result = calculations(result, perm[i-1], numbers[i])
    max_value = max(max_value, result)
    min_value = min(min_value, result)
  return max_value, min_value

N = int(input())
numbers = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))

max_result, min_result = find_max_min(N, numbers, operator_counts)
print(max_result)
print(min_result)
