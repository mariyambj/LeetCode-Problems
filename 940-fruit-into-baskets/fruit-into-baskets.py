class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        basket=[]
        count={}
        max_fruit=0
        for end in range(len(fruits)):
            if fruits[end] not in count:
                count[fruits[end]]=0
            count[fruits[end]]+=1
            while len(count)>2:
                count[fruits[start]]-=1
                if count[fruits[start]]==0:
                    del count[fruits[start]]
                start+=1
            max_fruit=max(max_fruit,end-start+1)
        return max_fruit



        