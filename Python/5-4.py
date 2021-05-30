#이것이 코딩테스트다. with 파이썬

#재귀 함수 종료 예제 5-4

def recursive_function(i):
    if i == 3:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

#<출력>
# 1 번째 재귀 함수에서 2 번째 재귀 함수를 호출합니다.
# 2 번째 재귀 함수에서 3 번째 재귀 함수를 호출합니다.
# 2 번째 재귀 함수를 종료합니다.
# 1 번째 재귀 함수를 종료합니다.
