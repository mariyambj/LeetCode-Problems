class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start,path,new_target):
            if new_target==0:
                result.append(path[:])
            if new_target<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                remaining=new_target-candidates[i]
                backtrack(i+1,path,remaining)
                path.pop()
        backtrack(0,[],target)
        return result