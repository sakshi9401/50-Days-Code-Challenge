M = input()
M_set =set(map(int, input().split()))
N = input()
N_set =set(map(int, input().split()))
M_diff = M_set.difference(N_set)
N_diff = N_set.symmetric_difference(M_set)
common = M_diff.union(N_diff)
for i in sorted(common):
    print(i)    
