def solution(n):
    num = []
    n = str(n)
    
    for i in range(len(n)):
        num.append(n[i])
    num.sort()
    num.reverse()

    return int(''.join(num))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(118372))



#<풀이>
#저는 정수를 배열로 바꿔 sort 시키고 reverse해서 다시 문자열로 변경하고 정수로 변경하는 방법으로 해결했는데..
#list(str(n)) 이 있었네요ㅎㅎ
#저렇게 간단하게 풀 수 있었.. 😂
#
#하하 너무 재밌습니다.

#<최적코드>
def solution(n): 
    ls = list(str(n)) 
    ls.sort(reverse=True) 
    return int(''.join(ls)) 
# 아래는 테스트로 출력해 보기 위한 코드입니다. 
print(solution(118372))
