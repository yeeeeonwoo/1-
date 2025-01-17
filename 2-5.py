from itertools import combinations

# 팀의 총 능력치를 계산하는 함수, team은 팀 내에서 사람들의 번호 team[0]은 그 팀 중에 1번임(기존 선수번호와는 달라)
def team_ability(team, score):
  total_score = 0
  for i in range(len(team)):
    for j in range(i+1, len(team)):
      total_score += score[team[i]][team[j]] + score[team[j]][team[i]]
  return total_score

def min_diff(N, score):
  players = list(range(N))
  min_difference = float('inf')

  # N명을 반으로 나누는 조합
  for start_team in combinations(players, N//2):
    start_team = list(start_team)
    link_team = [player for player in players if player not in start_team]
    # 팀이 나눠지는 모든 경우에 대한 능력치 계산
    start_score = team_ability(start_team, score)
    link_score = team_ability(link_team, score)

    # 능력치 차이 계산
    difference = abs(start_score - link_score)
    min_difference = min(min_difference, difference)

    if min_difference == 0:
      break

  return min_difference


N = int(input())
score = [list(map(int, input().split())) for _ in range(N)]
print(min_diff(N, score))
