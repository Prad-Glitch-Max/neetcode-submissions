class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference=target-nums[i]
            j=0
            if difference in nums:
                j=nums.index(difference)
                if i!=j:
                    if i<j:
                        return [i,j]
                    else:
                        return [j,i]

