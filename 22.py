def count_number_4(nums):
    count = 0
    for num in nums:
        if num == 4:
            count += 1
    return count
print(count_number_4([1,2,4,5,4]))
print(count_number_4([4,2,4,5,2,4]))