def trap(height):
    n = len(height)
    left, right = 0, n - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


if __name__ == "__main__":
    arr = list(map(int, input("Enter bar heights: ").split()))
    print("Trapped water:", trap(arr))
