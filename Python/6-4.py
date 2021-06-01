# 이것이 코딩 테스트다 with 파이썬

# 퀵 정렬 소스코드 6-4
# 가장 많이 사용되는 알고리즘
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈
# 피벗(pivot)이 사용됨 - 교환하기 위한 기준
# 피벗을 정하고 왼쪽부터는 피벗보다 큰 값을, 오른쪽 부터는 피벗보다 작은 값을 찾아 위치를 바꿈
# 만약 서로 엇갈렸다면 작은값과 피벗의 위치를 변경

array = [5, 7, 9, 0, 3, 1, 5, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번쨰 원소
    left = start + 1
    right = end

    while left<= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
        # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) -1)
print(array)


# <출력>
# [0, 1, 2, 3, 4, 5, 5, 7, 8, 9]
