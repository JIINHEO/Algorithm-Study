# 이것이 코딩테스트다 with 파이썬

# 문제 6-10
# 위에서 아래로
# 수열을 내림차순으로 정렬하는 프로그램 만들기

# <풀이>
# bfs를 이용했을 때 매우 효과적 (시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문)
# (1,1) 지점에서부터 bfs를 수행하여 모든 노드의 값을 거리 정보로 넣으면 된다.
# 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣는다.

n = int(input())
array =[]
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')

# <입력>
# 3
# 15
# 27
# 12

# <출력>
# 27 15 12
