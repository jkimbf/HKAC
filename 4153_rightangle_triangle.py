while True:
    a, b, c = [int(x) for x in sorted(map(int, input().split()))]
    print("{}\t{}\t{}".format(a,b,c))
    if a+b+c == 0: break
    if c**2 == (a**2 + b**2):
        print('right')
    else:
        print('wrong')

