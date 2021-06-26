def solution(arr1, arr2):
    for i in range (len(arr1)) : # 행
        for j in range (len(arr1[0])): # 열
            arr1[i][j] += arr2[i][j]
    return  arr1
