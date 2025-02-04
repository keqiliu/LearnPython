import random

# A[i] is a one-dimension array with both positive and negative numbers
# find the maximum sum from subarray A[i,j], where 1<=i<=j<=n


def find_max_sub(A):
    """
    define V[i,j] = sum of A[i,j]
           M[i] = A[1]+A[2]+...+A[i]
    we have V[i,j] = M[j] - M[i-1]
    to find max(V[i,j]), for any given j, 
    we want to minimize M[t], where t = 1, 2,... j-1
    i.e. to track min(0, M[1], M[2], ... M[j-1])
    we have 0 here, because if everything is positive, then we do
    V[i,j] = M[j] - 0 = M[j]
    """

    M = A[0]
    min_m = min(0, A[0])
    V = A[0]

    for j in range(1, len(A)):
        M += A[j]
        # here, minM saves min(M[1], ..., M[i-1])
        V = max(V, M - min_m)
        min_m = min(min_m, M)

    return V


A = [random.randint(-100, 100) for _ in range(10)]
print(f'A = {A}')
print(f'max sub = {find_max_sub(A)}')