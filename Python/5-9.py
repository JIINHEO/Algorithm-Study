# 이것이 코딩테스트다. with 파이썬

# BFS 예제 5-9
# BFS는 큐 자료구조를 이용하는 것이 정석
# deque 라이브러리를 사용하는 것이 좋으며 탐색을 수행함에 있어 O(N)의 시간이 소요된다.
# 보통 DFS 보다는 BFS 구현이 조금 더 빠르게 동작한다.

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [ #총 9
    [], # 0번 노드에 대한 내용은 비워줌
    [2, 4, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9 #방문 False로 초9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited) #현재노드 1부터 시작


# <출력>
# 1 2 4 8 7 3 5 6 

