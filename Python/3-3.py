# 이것이 코딩테스트다. with 파이썬

# 문제 3-3
# 숫자 카드 게임
# 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임

# 1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. (행,열)
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 떄, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로
#     가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# <풀이>
# 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는것
# min() 함수를 이용할 수 있거나, 2중 반복문 구조를 이요할 수 있어야 한다.

n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n): # n행만큼 반복
    data = list(map(int, input().split())) # 행 입력
    min_value = min(data) # 행에서 제일 작은 수 찾기
    result = max(result, min_value) # 작은 수 들중에서 큰 수 찾기

print(result)


# <입력>
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# <출력>
# 2

