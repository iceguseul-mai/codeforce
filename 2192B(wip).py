import sys
input = sys.stdin.readline

def op(arr, i):
    print('start')
    for num in range(len(arr)):
        if num != i:
            if arr[num] == '0':
                arr[num] = '1'
            elif arr[num] == '1':
                arr[num] = '0'
    return arr

for _ in range(int(input())):
    n = int(input())
    a = list(input().rstrip())
    cnt = 0
    ans = []
    visit = set()
    flag = True
    while True:
        print(a)
        if str(a) not in visit:
            visit.add(str(a))
            for i in range(n):
                if a[i] == '1':
                    cnt += 1
                    ans.append(i+1)
                    a = op(a, i)
                    break
            if a.count('1') == 0:
                break
        else:
            flag = False
            break
    if flag == False:
        print(-1)
    else:
        print(cnt)
        print(*ans)