#이것이 코딩테스트다. with 파이썬

#예제 4-1

#<입력 조건>
#첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
#둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동횟수 <= 100)

#<출력 조건>
#첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X, Y)를 공백으로 구분하여 출력한다.

#<풀이>

#N을 입력받기
n = int(input())

#이동 방향 입력 받기
plans = input().split()

x, y = 1, 1

#L, R, U, D에 따른 이동 방향
#(dx,dy)로 각 L = (0,-1) R = (0, 1)...
dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    #이동 수행
    x, y = nx, ny

print(x, y)

#연산 횟수는 이동 횟수에 비례하게 된다.
#이동 횟수가 N번인 경우 시간 복잡도는 O(N)이다.
