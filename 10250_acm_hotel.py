num_test = int(input())
for _ in range(num_test):
	H, W, N = map(int, input().split())
	floor = H if (N % H) == 0 else (N % H)
	room_num = (N // H) if (N // H) == (N / H) else (N // H + 1)
	print('{}{:02}'.format(floor, room_num))
