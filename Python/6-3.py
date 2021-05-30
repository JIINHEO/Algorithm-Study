# 이것이 코딩테스트다. with 파이썬

# 삽입 정렬 예제 6-3
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 '삽입'
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작
# 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
# 필요할때만 위치를 바꾸므로 '데이터가 거의 정렬되어 있을 때' 훨씬 효율적
# 두번째 데이터부터 시작, 첫 번쨰 데이터는 그 자체로 정렬되어 있다고 판단하기 때문
# 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
# 시간 복잡도 O(n^2) 최선의 경우 O(N)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번쨰 원소부터 시작해서 왼쪽으로 이동해나가면서 위치를 바꿔줌
    for j in range(i, 0, -1):       # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:   # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)

# <출력>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

