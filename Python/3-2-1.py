# 이것이 코딩테스트다. with 파이썬

# 문제 3-2
# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 특징

# <풀이>
# 입력값 중에서 가장 큰 수와 두번쨰로 큰 수만 저장하면 된다.
# 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번쨰로 큰 수를 한 번 더하는 연산'을 반복하면 된다.

# N, M, K 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() #입력 받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번쨰로 큰 수

result = 0

while True : # 5, 8, 3
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 # 더할 때마다 1씩 뺴기

    if m == 0: #m이 0이라면 반복문 탈출
        break
    result += second # 두 번쨰로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1 씩 뺴기

print(result) # 최종 답안 출력

# <출력>
# 46




# <다른 풀이>
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = 0
for i in range(1, m+1): # m번만큼 반복할거야

    if i % k != 0:
        result += data[0]
    else:
        result += data[1]

print(result)

