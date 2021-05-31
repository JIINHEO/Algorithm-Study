# 이것이 코딩테스트다 with 파이썬

# 문제 4-4 (2중 반복문 구조를 이용)
# 게임 개발
# 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력해라.

# (A, B) 바다로 되어 있는 공간에는 갈 수 없다
# 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향 )부터 차례대로 갈 곳을 정한다.
# 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
#    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향으로 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
#    단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

# <풀이>
# 좌로 회전 후 앞이 바다 또는 방문한 장소라면 왼쪽 회전 횟수를 센다 
# 횟수가 4가 되면 현재 방향에서 뒤로 한칸 이동한다, 하지만 뒤가 바다라면 멈춘다.
# 위에 해당하지 않으면 반복문 처음으로 돌아간다.
# 처음으로 안돌아가면 좌로 이동이 가능하므로 현재 위치를 갱신한다.

# 좌로회전 -> 앞이 이동 가능하면 이동 -> 아니면 왼쪽 회전 횟수 체크 -> 회전 횟수가 4이면 현재 바라보고 있는 방향에서 뒤로 한칸 이동 
# -> 이때 뒤가 바다면 멈춤


# 입력 받기
n, m = map(int, input().split())
# 3 <= N, M <= 50

# 0 으로 초기화 N , M
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 맵 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 (방향 입력)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전시키는 메서드
def turn_left():
    global direction
    direction -= 1 # (왼쪽(반시계 방향)으로 회전하니까 index를 북 -> 동 -> 남 -> 서 순으로 -1을 해줌)
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1 # 첫번째 이미 방문으로 초기화
turn_time = 0

while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0 # 횟수 초기화
        continue

    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

# <입력>
# 4 4 // 4 x 4 맵 생성
# 1 1 0 // (1,1)에 북쪽(0)을 바라보고 서 있는 캐릭터
# 1 1 1 1 // 첫 줄은 모두 바다
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# <출력>
# 3
