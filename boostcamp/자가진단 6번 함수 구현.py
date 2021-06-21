def solution(arr):
    answer = []

    while(0 < len(arr)):    # arr의 원소가 다 없어질때까지 반복

        item = arr[0]       		  # 중복을 확인할 숫자
        
        if arr.count(item) > 1: # 중복값이 있다면
            answer.append(arr.count(item)) # 중복횟수를 배열 answer에 넣고
            for i in range(arr.count(item)): # 중복횟수만큼 해당숫자(item)를 배열 arr에서 삭제
                arr.remove(item)
        else:                   # 중복값이 없으면
            arr.remove(item)    # 해당 숫자만 배열arr에서 삭제

    return answer if len(answer) else -1 # 배열 answer에 원소가 들어있다면 answer를 반환하고, 
    					 # 아니면 -1을 반환

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
print(solution([3, 5, 7, 9, 1]))

