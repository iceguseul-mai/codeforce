import sys, statistics
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int,input().split())
    c = sorted(list(map(int, input().split())))
    ans = n
    modes = statistics.multimode(c)
    standard = max(modes)
    std_divide = 0
    if standard % 2 == 1:
        ccount1 = 0
        ccount2 = 0
        if c[i] > std_divide:
                    c.append(c[i]-std_divide)
    else:
        std_divide = standard//2
    for i in range(n):
        if c[i] > std_divide:
            c.append(c[i]-std_divide)
            c[i] = std_divide
    print(max(ans, c.count(std_divide)))