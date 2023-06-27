def quicksort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    base = arr[0]
    left = [arr[i] for i in range(1, n) if arr[i] < base]
    right = [arr[j] for j in range(1, n) if arr[j] > base]
    return quicksort(left) + [base] + quicksort(right)


if __name__ == '__main__':
    lis1 = list(map(int, input().split(" ")))
    print(quicksort(lis1))
