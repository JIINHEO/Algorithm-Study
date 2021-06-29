def solution(s):
    answer = ''
    s = s.split(' ')

    for i in s:
        if i == '': # 공백일 경우 처리
            answer += ' '
        else:
            answer += i.capitalize()
            answer += ' '

    answer = answer[:-1]
    return answer
  
  
# 테스트케이스 몇개가 실패해서 왜그러는지 한참 찾았네요 !!!!
# 문자열 s 는 알파벳과 공백으로 이루어져있다.
# 공백!!!! 공백이 앞에도..뒤에도.. 여러개도 있을 수 있다는거!! 생각을 못했네요 ㅠㅠ
# 예를 들면 "    aa     bb cc  " 이럴 경우 에러가 납니다. !
# 그래서 공백을 처리하는 코드를 넣어주었습니다. !!!  

# 출처: https://jiinheo.tistory.com/88 [코딩하는 지니]
