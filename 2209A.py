import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, cp, ff = map(int, input().split())
    a = list(map(int, input().split()))
    while len(a) != 0 and min(a) <= cp:
        for i in a:
            if i <= cp:
                if cp-i > ff:
                    cp += (i + ff)
                    ff=0
                    a.remove(i)
                else:
                    ff -= cp-i
                    cp += cp
                    a.remove(i)
    print(cp)

