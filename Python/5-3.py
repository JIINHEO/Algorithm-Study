#이것이 코딩테스트다. with 파이썬

#재귀 함수 예제 5-3

def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()

# RecursionError: maximum recursion depth exceeded while pickling an object
# 재귀의 최대 깊이를 초과했기 때문에 오류가 생김
