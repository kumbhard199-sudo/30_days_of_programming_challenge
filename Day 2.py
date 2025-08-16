def find_missing_number(arr):
    n= max(arr)
    full_set=set(range(1,n+1))
    arr_set=set(arr)
    missing=sorted(list(full_set-arr_set))
    return missing
arr=list(map(int, input("enter numbers:").split()))
print("Missing number:",find_missing_number(arr))
