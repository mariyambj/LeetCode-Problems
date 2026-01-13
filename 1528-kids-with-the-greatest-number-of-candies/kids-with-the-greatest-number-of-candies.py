class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        i=0
        max_candies=max(candies)
        while i<len(candies):
            if candies[i]+extraCandies >= max_candies:
                result.append(True)
                i+=1
            else:
                result.append(False)
                i+=1
        return result
