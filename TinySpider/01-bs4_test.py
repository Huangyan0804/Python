
#print(a, b, c, d, e, f, g)
t = int(input())
for i in range(t):
    a, b, c, d, e, f, g = map(int, input().split())
    if a**d + b**e + c ** f == g:
        print('Yes')
    else:
        print('No')
