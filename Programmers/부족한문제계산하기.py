def solution(price, money, count):
    num = []
    for i in range(1, count+1):
        num.append(price * i)
    result = sum(num)
    if result > money :
        return result - money
    else : return 0


# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print(solution(3, 20, 4))
