def solution(n):
    for i in range(n, n+10):
        lists = []
        b = i
        while b > 0:  # 2진수 변환
            a = b % 2  # 나머지
            b = b // 2  # 몫
            lists.append(a)
        lists.reverse()
        if n == i :
            count = lists.count(1)
        else:
            if count == lists.count(1):
                return i

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution(78))
print(solution(15))
