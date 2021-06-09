import copy 

test_nums = [ 2, 3, 4, 6, 5 ]

# O(?)
def inversions( nums: list) -> int:
    # recursion anker
    if 1 == len(nums):
        return 0
    
    # split list
    mid_i = int(len(nums) / 2)
    inv_cnt = 0

    # count inversions between lists
    for i in range(mid_i):
        for j in range(mid_i):
            if nums[i] > nums[mid_i + j]:
                inv_cnt += 1

    inv_cnt += inversions(nums[:mid_i])
    inv_cnt += inversions(nums[mid_i:])
    return inv_cnt 


