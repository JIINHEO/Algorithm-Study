# 이것이 코딩테스트다 with 파이썬

# 문제 6-11
# 성적이 낮은 순서로 학생 출력하기
# 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램

# <풀이>
# 

n = int(input())
array = []

for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

print(array)

# 키(key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')

# <입력>
# 2
# 홍길동 95
# 이순신 77

# <출력>
# 이순신 홍길동
