# n = int(input())
# out = [1, 2] + [0]*(n-2)
# for i in range(2, n):
#     out[i] += sum(out[i-2:i])
# print(out[n-1] % 10007)

# n = int(input())
# out = [1, 2]
# for i in range(2, n):
#     out.append(sum(out[i-2:i]))
# print(out[n-1] % 10007)

n = int(input())
out = [1, 2]
for i in range(2, n):
    out[i%2] += out[(i+1)%2]
print(out[(n-1)%2] % 10007)