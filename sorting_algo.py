
def quick_sort(nums, start, end):
    if not nums:
        return []
    
    if start < end:
        partition_idx = partition(nums, start, end)
        quick_sort(nums, start, partition_idx - 1)
        quick_sort(nums, partition_idx + 1, end)

def partition(nums, start, end):
    pivot = nums[end]
    lower = start - 1 # KEY: start - 1
    
    for i in range(start, end):
        if nums[i] < pivot:
            lower += 1
            nums[lower], nums[i] = nums[i], nums[lower]

    nums[lower + 1], nums[end] = nums[end], nums[lower + 1] # KEY: switch pivot to the right index at the end
    return lower + 1


def mergesort(nums):
    if len(nums) <= 1:
        return

    mid = len(nums) // 2
    l = nums[:mid]
    r = nums[mid:]
    mergesort(l)
    mergesort(r)

    i, j, k = 0, 0, 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            nums[k] = l[i]
            i += 1
        else:
            nums[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        nums[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        nums[k] = r[j]
        j += 1
        k += 1

nums = [3,4,5,1,6,2]
#quick_sort(nums, 0, len(nums) - 1)
mergesort(nums)
print(nums)