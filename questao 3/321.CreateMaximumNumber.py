class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def everymax(nums,n):
            stack=[]
            to_pop=len(nums)-n
            for num in nums:
                while to_pop and stack and num>stack[-1]:
                    stack.pop()
                    to_pop-=1
                stack.append(num)
            return stack[:n]

        def merge(nums1,nums2):
            result=[]
            while nums1 and nums2:
                if nums1>nums2:
                    result.append(nums1[0])
                    nums1=nums1[1:]
                else:
                    result.append(nums2[0])
                    nums2=nums2[1:]
            result.extend(nums1)
            result.extend(nums2)
            return result

        ans=[]
        for i in range(k+1):
            if i <=len(nums1) and (k-i)<=len(nums2):
                maxnums1=everymax(nums1,i)
                maxnums2=everymax(nums2,k-i)
                merged=merge(maxnums1,maxnums2)
                ans=max(ans,merged)
        return ans