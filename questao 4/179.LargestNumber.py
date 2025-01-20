class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            nums[i] = str(nums[i])
        
        if count == len(nums):
            return '0'

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if int(nums[j] + nums[i]) > int(nums[i] + nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        return ''.join(nums)