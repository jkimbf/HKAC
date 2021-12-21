from sys import stdin
print(*sorted(int(num.strip()) for num in stdin.readlines()[1:]), sep='\n')