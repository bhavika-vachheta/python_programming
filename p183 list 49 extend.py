def check_first_last(nums):
    if len(nums) < 2:
        return False
    return nums[0] == nums[-1]
list1 = [100, 200, 320, 40, 100]
list2 = [751, 6, 3, 5, 9]
print("List 1 result:", check_first_last(list1))
print("List 2 result:", check_first_last(list2))
