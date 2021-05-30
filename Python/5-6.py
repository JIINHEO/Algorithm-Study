# 이것이 코딩테스트다. with 파이썬

# 인접 행렬 방식 예제 5-6
# 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.

INF = 999999999 #무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0,7,5],
    [7,0,INF],
    [5, INF, 0]
]

print(graph)

#<출력>
#[[0, 7, 5], [7, 0, 999999999], [5, 999999999, 0]]
