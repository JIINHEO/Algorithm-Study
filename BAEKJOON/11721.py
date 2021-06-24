a = input()
answer = ''
j = 0
for i in range(int(len(a)//10)+1):
    answer += a[i+j:i+j+10]
    answer += "\n"
    j+=9

print(answer)
