import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int,input().split()))
    if sum(a)%2 == 1 or (n*k-1)%2 == 1:
        print("YES")
    else:
        print("NO")