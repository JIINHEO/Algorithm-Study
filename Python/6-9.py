# 이것이 코딩 테스트다 with 파이썬

# 정렬 라이브러리에서 key를 활용한 소스코드 6-9

array = [('바나나', 2),('사과', 5),('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
