class Solution:
    def compressedString(self, word: str) -> str:
        read=0
        result=""
        while read<len(word):
            cur_read=word[read]
            count=0
            while read<len(word) and cur_read==word[read] and count<9:
                read+=1
                count+=1
            result+=str(count)
            result+=cur_read
        return result

        