# This concept will be used to find num of pairs, basically all such problems, where one is suppose to find relationship between two nums of an array and it can be between any two numbers of an array

# Find number of pairs whose absolute difference is less than diff

def main(diff,nums):
    l = 0
    total = 0
    nums.sort()
    for r in range(1,len(nums)):
        while nums[r]-nums[l] > diff:
            l += 1
        total += r-l
    return total

nums = [1,5,4,9,8,6,9,9,7,10,10]
diff = 2
print(main(diff,nums))