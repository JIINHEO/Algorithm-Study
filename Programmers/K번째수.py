def solution(array, commands):
    answer = []

    for i in range(len(commands)):
        answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))



# <다른 풀이>


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append((sorted(array[i - 1:j]))[k - 1])
    return answer

  
# or

def solution(array, commands):
  return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
