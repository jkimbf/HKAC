N, M = map(int, input().split())
input_board = []

for i in range(N):
	input_board.append(list(input()))

def count_incorrect(arr):
	counts = []
	for start_char in ['B', 'W']:
		count = 0
		start_arr = [r[i%2::2] for i, r in enumerate(arr)]
		count += sum([x.count(start_char) for x in start_arr])
		
		next_char = 'W' if start_char == 'B' else 'B'
		next_arr = [r[(i+1)%2::2] for i, r in enumerate(arr)]
		count += sum([x.count(next_char) for x in next_arr])
		counts.append(64-count)
	return min(counts)

counts = []
for i in range(N-8+1):
	for j in range(M-8+1):
		temp_board = [x[j:j+8] for x in input_board[i:i+8]]
		counts.append(count_incorrect(temp_board))

print(min(counts))
