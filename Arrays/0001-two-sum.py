class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n=len(nums)
        ans=[]
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]== target:
                    ans.append(i)
                    ans.append(j)
        return ans


# Test case
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))

