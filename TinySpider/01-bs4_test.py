
#print(a, b, c, d, e, f, g)


def work(x, a, b):
    if x == 0:
        return a + b
    else:
        return work(x - 1, a * 2, a)


t = int(input())
for i in range(t):
    n = int(input())
    ans = work(n, int(1), int(0))
    print(ans)

