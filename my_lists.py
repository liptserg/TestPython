

def main():
    a = [4, 5, 6, 5]
    b = [7, 15, 9, 50]
    print(list(zip(a, b)))
    print(*zip(a, b))
    print(*map(lambda x: x*x if x%2 ==0 else x, b))
    converter = lambda x : x*2 if x < 10 else (x*3 if x < 20 else x)
    print(*map(converter, b))

    c = 80
    d = 25
    while c != 0 and d != 0:
        if c > d:
            c %= d
        else:
            d %= c
    print(d+c)

    i = iter(a)
    print(next(i))
    print(next(i))
    print(next(i))

    print(c)

main()
