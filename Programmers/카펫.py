def solution(brown, yellow):

    total = brown + yellow

    for i in range(1, total):
        m = (int((yellow)/i)+2) 
        n = 2+i
        if n * m == total and (n-2)*(m-2) == yellow:
            return [m , n]

# 아래는 테스트를 위한 출력 코드입니다.
print(solution(10, 2))
print(solution(8,1))
print(solution(24, 24))
print(solution(44, 100))
