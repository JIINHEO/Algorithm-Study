# 이것이 코딩테스트다 with 파이썬

# 문제 3-5 (2중 반복문 구조를 이용)
# 1이 될 때까지
# N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수 구하기

# 1. N에서 1을 뺀다.
# 2. N에서 K로 나눈다.

# <풀이>
# N이 K의 배수가 될 때까지 1씩 뺴기
# N을 K로 나누기

n, k = map(int, input().split())
result = 0

while True:
    # n == k 로 나누어 떨어지는 수 가 될때까지 1씩 빼기
    target = (n//k) * k
    result += (n - target) # -1을 하고 횟수를 result에 더해줌
    n = target 

    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
        
    # k로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# <입력>
# 25 5

# <출력>
# 2

