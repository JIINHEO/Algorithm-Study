def solution(priorities, location):
    count = 0

    while priorities:  # priorities가 없어질때까지
        print(priorities)
        if location == 0 : # 출력 순서일 경우
            if priorities[0] < max(priorities): # 더 중요한 문서가 있으면
                priorities.append(priorities.pop(0)) # 맨뒤로 보냄
                location = len(priorities) -1 # location을 맨 끝으로 설정
            else: # 없으면 내꺼 출력
                return count +1
        else :
            if priorities[0] < max(priorities):
                priorities.append(priorities.pop(0)) # 맨뒤로 보냄
                location -= 1 # 맨앞 요소가 뒤로 갔기 때문 -1
            else:
                print("location = ",location)
                priorities.pop(0) #맨 앞 요소 출력
                location -= 1 # 맨앞 요소가 뒤로 갔기 때문 -1
                count += 1 # 출력번쨰수 +1

# 아래는 테스트로 출력해보기 위한 코드입니다.
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
