def solution(progresses, speeds):
    count = 0
    answer = []
    
    while (len(progresses)):  # progresses 에 원소가 있을때까지

        if progresses[0] < 100:  # 100보다 작으면 계속 더해라
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        if progresses[0] >= 100:  # 배포 가능하면 배포해라
            for i in range(len(progresses)):
                if progresses[0] >= 100:
                    progresses.pop(0)
                    speeds.pop(0)
                    count += 1
            answer.append(count)
            count =0

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
