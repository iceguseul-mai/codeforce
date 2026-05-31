import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(len(str(n))-str(n).count('0'))
    ans = []
    exp = 10**(len(str(n))-1)
    for i in range(1, len(str(n))+1):
        if int(str(n)[i-1])*exp != 0:
            ans.append(int(str(n)[i-1])*exp)
        exp //= 10
    print(*ans)