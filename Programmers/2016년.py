def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU',]
    dd = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i = 0

    for m in range(1, a+1): # 1-12월
        for d in range(1, dd[m-1]+1): # 1-31일
            result = day[(i+d-1) % 7]
            if m == a and d == b:
                return result
        i += dd[m-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution(5, 24))

# 1.31 2.29(윤년) 3.31 4.30 5.31 6.30 7.31 8.31 9.30 10.31 11.30 12.31


# <다른 풀이>

def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
