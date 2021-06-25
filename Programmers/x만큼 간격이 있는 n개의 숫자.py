def solution(x, n):
    answer = []
    num = x
    for i in range(n):
        answer.append(num)
        num += x
    return answer
