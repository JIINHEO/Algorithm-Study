def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([4,3,2,1]))



# <풀이>
# else: 
#      min_num = arr[0] 
#      for i in range(1, len(arr)):
#           min_num = min(min_num, arr[i]) 
#     arr.remove(min_num)
#     return arr

# 처음에 min(arr) 를 할 생각을 못하고 for문으로 최솟값을 찾고있었네요 😂
# min()은 사용하면서.. min(arr)는 생각을 못하다니.. 하.. 😔

# remove(value)랑 pop(index)이랑 고민했는데 만약 최솟값이 1,1,1 처럼 여러개라면 
# remove를 쓰는게 맞다고 생각해서 remove를 사용했습니다.

# 너무 재미있습니다. 🥰
