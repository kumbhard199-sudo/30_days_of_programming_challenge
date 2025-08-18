def merge(arr1, arr2, m, n):
    def nextGap(gap):
        if gap <= 1:
            return 0
        return (gap // 2) + (gap % 2)

    gap = m + n
    gap = nextGap(gap)

    while gap > 0:
        i = 0
        j = gap
        while j < m + n:
            
            if i < m and j < m:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            
            elif i < m and j >= m:
                if arr1[i] > arr2[j - m]:
                    arr1[i], arr2[j - m] = arr2[j - m], arr1[i]

           
            else:
                if arr2[i - m] > arr2[j - m]:
                    arr2[i - m], arr2[j - m] = arr2[j - m], arr2[i - m]

            i += 1
            j += 1

        gap = nextGap(gap)


m = int(input("Enter size of 1st array(arr1): "))
arr1 = list(map(int, input("Enter elements of arr1 : ").split()))
n = int(input("Enter size of 2nd array(arr2): "))
arr2 = list(map(int, input("Enter elements of arr2 : ").split()))

merge(arr1, arr2, m, n)

print("Merged arr1:", arr1)
print("Merged arr2:", arr2)
