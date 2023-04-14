
# 파기일을 지정해놓은 dictionary를 만들거임
# "2022.05.19"	["A 6", "B 12", "C 3"]	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# 각 a, b, c 에 해당하는 날짜를 만들자
# dic[a] = 202111119 뭐 이런식으로
# dic[b] = 20210519
# dic[c] = 20220219 이 이후에 발행된것만 가능함 만약 발급 날짜가 이거보다 작으면 파기해야함
# 그리고 문자열 잘라서 A이네? 20220219(발행날짜) < 20220219(최소 발행일자) 이면 arr.append(index)

# 모든 달은 28일까지 있다고 가정합니다. 기준이 28일이었어......시바

def solution(today, terms, privacies):
    answer = []
    dic = {}
    today = today.replace('.', '')

    for item in terms:
        arr = item.split(' ')
        dic[arr[0]] = int(arr[1])

    for i in range(0, len(privacies)):
        arr = privacies[i].split(' ')
        day = int(arr[0].replace('.',''))
        file = arr[1]
        day += (dic[file] * 100) - 1
        if str(day)[6:] == '00':
            day -= (100-28)
        if str(day)[4:6] > '12':
            day -= 1200
            day += 10000
        if day < int(today):
            answer.append(i+1)

    return answer
