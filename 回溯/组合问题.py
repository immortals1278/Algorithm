def func(n,k):
    result = []
    def func1(n,k,arr,j):
        if len(arr) == k:
            result.append(arr)
            return
        if j <= n:
            func1(n, k, arr, j + 1)
        if j <= n:
            func1(n, k, arr + [j], j + 1)

    func1(n,k,[],1)
    return result


n, k = map(int, input().split())
res = func(n,k)[::-1]
print(res)

