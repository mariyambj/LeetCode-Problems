class Solution:
    def maxRepOpt1(self, text: str) -> int:
        char_count=[]
        count=1
        total_count=Counter(text)
        for i in range(1,len(text)):
            if text[i]==text[i-1]:
                count+=1
            else:
                char_count.append((text[i-1],count))
                count=1
        char_count.append((text[-1],count))
        max_len=0
        for char,length in char_count:
            if total_count[char]>length:
                max_len=max(max_len,length+1)
            else:
                max_len=max(max_len,length)
        for i in range(1, len(char_count) - 1):
            prev_char, prev_len = char_count[i-1]
            mid_char, mid_len = char_count[i]
            next_char, next_len = char_count[i+1]
            
            if prev_char == next_char and mid_len == 1:
                combined = prev_len + next_len
                if total_count[prev_char] > combined:
                    max_len = max(max_len, combined + 1)
                else:
                    max_len = max(max_len, combined)
        return max_len


