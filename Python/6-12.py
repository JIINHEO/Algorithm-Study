# 이것이 코딩테스트다 with 파이썬

# 문제 6-12
# 두 배열의 원소 교체
# 배열 A의 원소의 합이 최댓값을 출력하는 프로그램

# 최대 K번 바꿔치기 연산을 수행할 수 있는데,
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는것
# 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는것

# <풀이>
# 배열 A에서 가장 작은 원소와 배열 B에서 가장 큰 원소를 교체한다.

n, k = map(int, input().split())

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

arr_A.sort()
arr_B.sort(reverse=True)

for i in range (k):
    if arr_A[i] < arr_B[i] : #작다면 바꾸자
        arr_A[i], arr_B[i] = arr_B[i], arr_A[i]
        i +=1
    else:
        break

print(sum(arr_A))

# <입력>
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5

# <출력>
# 26
