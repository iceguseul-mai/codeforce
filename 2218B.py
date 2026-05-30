import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a = sorted(list(map(int, input().split())))
    print(a[6]-(a[5]+a[4]+a[3]+a[2]+a[1]+a[0]))