q1>def convert_to_2d_array(original, m, n):
    total_elements = len(original)
    if total_elements != m * n:
        return []

    result = [[0] * n for _ in range(m)]

    for i in range(total_elements):
        row = i // n
        col = i % n
        result[row][col] = original[i]

    return result
q2>def arrange_coins(n):
    row = 1
    while n >= row:
        n -= row
        row += 1
    return row - 1
q3>def sorted_squares(nums):
    result = []
    for num in nums:
        square = num * num
        result.append(square)
    result.sort()
    return result
q4>def find_disjoint(nums1, nums2):
    distinct_nums1 = list(set(nums1) - set(nums2))
    distinct_nums2 = list(set(nums2) - set(nums1))
    return [distinct_nums1, distinct_nums2]
q5>def find_distance(arr1, arr2, d):
    count = 0
    for num in arr1:
        for num2 in arr2:
            if abs(num - num2) <= d:
                break
        else:
            count += 1
    return count
q6>def find_duplicates(nums):
    result = []
    for num in nums:
        idx = abs(num) - 1
        if nums[idx] < 0:
            result.append(abs(num))
        else:
            nums[idx] = -nums[idx]
    return result
q7>def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
q8>from collections import defaultdict

def find_original_array(changed):
    count = defaultdict(int)

    for num in changed:
        count[num] += 1

    original = []

    for num in changed:
        if num % 2 != 0 or count[num] == 0:
            return []
        count[num] -= 1
        original.append(num // 2)

    return original
