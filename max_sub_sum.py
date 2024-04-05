# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSubArray_brute(nums):
    maxes = []
    for j in range(0,9):
            for i in range(0,9-j):
                num_slice = nums[i:i+1+j]
                maxes.append(sum(num_slice))
    return(max(maxes))   


print(maxSubArray_brute(nums))
    
    
def maxSubArray(nums):
    max_sum = current_sum = nums[0]
    
    
    for num in nums[1:]:
        print(max_sum)
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

print(maxSubArray(nums))
