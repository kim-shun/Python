def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            count += 1

    print(count)

count_evens([2, 1, 7, 8, 2, 3, 4])
count_evens([2, 2, 6, 5, 0]) 
count_evens([1, 3, 11, 5])
