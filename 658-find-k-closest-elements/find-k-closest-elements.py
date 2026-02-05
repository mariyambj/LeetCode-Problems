class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low=0
        high=len(arr) - k
        while low < high:
            mid= low+(high-low)//2
            if x <= arr[mid]:
                high=mid
            elif x>=arr[mid+k]:
                low=mid+1
            else:
                first=abs(x-arr[mid])
                second=abs(x-arr[mid+k])
                if first<=second:
                    high=mid
                else:
                    low=mid+1
        return arr[low:low+k]
        