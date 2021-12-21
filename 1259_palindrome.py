while True:
    num = input()
    if int(num) == 0: break
    size = len(num)
    is_palin = True
    for i in range(size//2):
        if num[i] != num[size-i-1]:
            print('no')
            is_palin = False
            break
    if is_palin:
        print('yes')

