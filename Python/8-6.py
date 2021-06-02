# 이것이 코딩 테스트다 with 파이썬

# 실전 문제 8-6
# 개미 전사
# 식량창고 N개에 대한 정보가 주어졌을 떄 얻을 수 있는 식략의 최댓값을 구해라

# 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

# 최적 부분 구조 - 특정 번 째 까지의 최적의 해는 i-1, i-2 로 계산될 수 있다.
# 중복되는 부분 문제
# ai = i 번째 식량 창고까지의 최적의 해
# ki = i 번째 식량 창고에 있는 식량의 양
# ai = max(ai-1, ai-2 + ki)

# 정수 N을 입력받기
n = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i -1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n-1])

# <입력>
# 4
# 1 3 1 5

# <출력>
# 8