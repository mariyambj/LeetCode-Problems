class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=[]
        reversed=""
        for i in s:
            if i in 'aeiouAEIOU':
                vowels.append(i)
        for i in s:
            if i in 'aeiouAEIOU':
                reversed+=vowels.pop()
            else:
                reversed+=i
        return reversed

   