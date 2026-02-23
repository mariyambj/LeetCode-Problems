class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied=0
        gain=[]
        for right in range(len(customers)):
            if grumpy[right]==0:
                satisfied+=customers[right]
                gain.append(0)
            else:
                gain.append(customers[right])
                       
        max_sum = cur_sum = sum(gain[0:minutes])
        for i in range(minutes, len(gain)):
            cur_sum = cur_sum + gain[i] - gain[i - minutes]
            max_sum = max(max_sum, cur_sum)
        return satisfied+max_sum
                
            
                

        