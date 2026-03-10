class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''nums.sort()
        quandrant=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while left<right:
                    sum_=nums[i] +nums[j] + nums[left] + nums[right]
                    if sum_==target:
                        quandrant.append([nums[i],nums[j],nums[left],nums[right]])  
                        left+=1
                        right-=1 
                    elif sum_ < target:
                        left+=1
                    else:
                        right-=1
        return quandrant'''

        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return [list(x) for x in ans]