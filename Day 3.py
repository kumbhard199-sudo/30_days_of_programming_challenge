def findDuplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:   
            return num
        seen.add(num)
    return -1   

arr = list(map(int, input("Enter numbers: ").split()))
print("Duplicate Number:", findDuplicate(arr))
