
# [44, 1, 0, 0, 31, 25] [31, 10, 45, 1, 6, 19] [3, 5]
# [0, 0, 0, 0, 0, 0] [38, 19, 20, 40, 15, 25] 1, 6
# [45, 4, 35, 20, 3, 9] [20, 9, 3, 45, 4, 35] 1, 1

def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zeroCnt = lottos.count(0)

    for i in range(6):
        for j in lottos:
            if j in win_nums:
                win_nums.remove(j)
                lottos.remove(j)
                cnt += 1

    answer.append(7 - zeroCnt - cnt)
    answer.append(7 - cnt)

    for i in range(2):
        if answer[i] == 0:
            answer[i] = 1
        elif answer[i] == 7:
            answer[i] = 6
    return answer

# def solution(lottos, win_nums):
#
#     rank=[6,6,5,4,3,2,1]
#
#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]