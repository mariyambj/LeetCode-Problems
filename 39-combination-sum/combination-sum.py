class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start,path,new_target):
            if new_target==0:
                result.append(path[:])
                return 
            if new_target<0:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                remaining_target=new_target-candidates[i]
                backtrack(i,path,remaining_target)
                path.pop()
        
        backtrack(0,[],target)
        return result


