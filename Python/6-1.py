# 이것이 코딩테스트다. with 파이썬

# 선택 정렬 예제 6-1
# 매번 '가장 작은 것을 선택' 하여 앞으로 보냄
# N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야한다.
# 시간 복잡도 O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index],array[i] #스와프

print(array)

# <출력>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

