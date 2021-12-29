N, r, c = map(int, input().split())
two2N = (2 ** N)
N2 = two2N ** 2
r_pos, c_pos = False, False
r_comp, c_comp = two2N, two2N
out = 0

for i in range(1, N+1):
    two2N //= 2
    r_comp = r_comp + two2N if r_pos else r_comp - two2N
    c_comp = c_comp + two2N if c_pos else c_comp - two2N
    
    r_pos = r >= r_comp
    c_pos = c >= c_comp

    N2 //= 4
    if r_pos and c_pos:
        out += N2 * 3
    elif r_pos and not c_pos:
        out += N2 * 2
    elif not r_pos and c_pos:
        out += N2 * 1

print(out)