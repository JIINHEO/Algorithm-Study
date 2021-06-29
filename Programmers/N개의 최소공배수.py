def solution(arr): #최대 공배수 구하기
    while len(arr) != 1:
        a = arr.pop()
        b = arr.pop()
        c = gcd(a,b)
        arr.insert(0, int(a*b/c))

    return arr[0]

def gcd(a,b): # 최대 공약수 구하기
    a, b = max(a,b), min (a,b)
    while b > 0:
        a,b = b, a%b
    return a


# 아래는 테스트를 위한 출력 코드입니다.
print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
