import operator

def solution(N, A, B):
    num_edges = [0] * N
    for a, b in zip(A, B):      # O(M)
        num_edges[a-1] += 1
        num_edges[b-1] += 1
    
    return sum(                 # O(N)
        map(operator.mul,       # + O(N)
            sorted(num_edges, reverse=True), 
            range(N, 0, -1)))

print(solution(5, [2,2,1,2], [1,3,4,4]))

