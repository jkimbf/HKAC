words = [input() for _ in range(int(input()))]
print(*sorted(set(words), key=lambda w: (len(w), w)), sep='\n')