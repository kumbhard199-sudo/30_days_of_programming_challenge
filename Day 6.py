def find_zero_sum_subarrays_brute(arr):
    result = []
    n = len(arr)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                result.append((i, j))
    return result

arr = list(map(int, input("Enter array elements : ").split()))
print("Zero sum subarrays:", find_zero_sum_subarrays_brute(arr))
