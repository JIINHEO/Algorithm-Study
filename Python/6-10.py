# 이것이 코딩테스트다 with 파이썬

# 문제 6-10
# 위에서 아래로
# 수열을 내림차순으로 정렬하는 프로그램 만들기

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
