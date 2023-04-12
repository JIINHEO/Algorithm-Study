# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
#
# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3

# https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = 0
    ch = [0] * (n+1)
    for i in range(2, n+1):
        if ch[i] == 0:
            answer += 1
            for j in range(i, n+1, i):
                ch[j] = 1
    return answer

# def solution(n):
#     num=set(range(2,n+1))
#
#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)



