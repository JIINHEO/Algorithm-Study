def solution(arr1, arr2):

    n = len(arr1)
    m = len(arr2[0])
    arr = []
    for i in range(n):
        arr.append([0]*m)

    for i in range(n):
        for j in range(m):
            sum =0
            for k in range(len(arr2)):
                sum += arr1[i][k] * arr2[k][j]
            arr[i][j] = sum
    return arr


# 아래는 테스트를 위한 출력 코드입니다.
print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
