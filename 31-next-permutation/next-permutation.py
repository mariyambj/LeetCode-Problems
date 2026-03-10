class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        for i in range(n-2 ,-1 ,-1):
            if nums[i + 1] > nums[i]:
                index = i 
                break
        
        if index == -1:
            self.rev(nums, 0, n -1)
            return 
        
        last = n - 1
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[index], nums[i] = nums[i], nums[index]
                break
        # print(nums)
        self.rev(nums, index + 1, n - 1)


    def rev(self, nums, s, e):
        while s < e:
            nums[s],nums[e] = nums[e], nums[s]
            s += 1
            e -= 1


