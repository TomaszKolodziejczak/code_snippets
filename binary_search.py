def binary_search(nums, target):
    left = 0
    right = len(nums)
    index = 0

    while left < right:
        index = (left + right) // 2

        if nums[index] == target:
            return index

        if nums[index] < target:
            left = index + 1

        if nums[index] > target:
            right = index

    return -1


if __name__ == '__main__':
    nums = [1, 3, 4, 5, 7, 9, 11, 15, 16, 17, 19]
    print(binary_search(nums, 11))
