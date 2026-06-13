import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = ['0'] + list(input().rstrip()) + ['0']
    ans = 0
    if n > 2:
        for i in range(1, n+1):
            if a[i-1] == '1' or a[i+1] == '1':
                a[i] = 2
        streak = 0
        for i in range(1, n+1):
            if a[i] == '0':
                streak += 1
            else:
                if streak != 0:
                    ans += (streak-1)//3+1
                streak = 0
        if streak != 0:
            ans += (streak-1)//3+1
        print(ans+a.count('1'))
    else:
        print(1)