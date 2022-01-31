from sys import stdin

out = {x: [None, None] for x in range(ord('A'), ord('Z')+1)}

for l in stdin.read().splitlines()[1:]:
    a,b,c = [x for x in map(ord, l.split())]
    if 0 <= b:
        out[a][0] = b
    if 0 <= c:
        out[a][1] = c

def print_tree(out, idx, type):
    if not ord('A') <= idx or out[idx] is None:
        return
    if type == 0:
        print(chr(idx), end='')
        print_tree(out, out[idx][0], type)
        print_tree(out, out[idx][1], type)
    elif type == 1:
        print_tree(out, out[idx][0], type)
        print(chr(idx), end='')
        print_tree(out, out[idx][1], type)
    elif type == 2:
        print_tree(out, out[idx][0], type)
        print_tree(out, out[idx][1], type)
        print(chr(idx), end='')

for i in range(3):
    print_tree(out, ord('A'), i)
    print()
