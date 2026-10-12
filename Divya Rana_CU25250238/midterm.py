
def solve():
    print("INPUT:")
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))

        for i in range(N):
            for j in range(i + 1, N):
                d1 = bin(A[i] ^ K).count('1')
                d2 = bin(A[j] ^ K).count('1')

                if d1 > d2 or (d1 == d2 and A[i] > A[j]):
                    A[i], A[j] = A[j], A[i]

        print("OUTPUT:")
        print(*A)


solve()
