# 문제 3-3
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

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번쨰로 큰 수 더하기

print(result) # 최종 답안 출력

# <출력>
# 46
