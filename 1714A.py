import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, h, m = map(int, input().split())
    alarm = set()
    for _ in range(n):
        alarm.add(tuple(map(int, input().split())))
    ansh, ansm = 0, 0
    curh, curm = h, m
    while (curh, curm) not in alarm:
        curm += 1
        if curm == 60:
            curm = 0
            curh += 1
        if curh == 24:
            curh = 0

        ansm += 1
        if ansm == 60:
            ansm = 0
            ansh += 1

    print(ansh, ansm)