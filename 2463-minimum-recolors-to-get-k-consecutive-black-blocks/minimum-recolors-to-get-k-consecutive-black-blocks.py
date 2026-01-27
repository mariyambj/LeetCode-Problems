class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_count=b_count=0
        white=0

        for i in range(k):
            if blocks[i]=='W':
                w_count+=1
        white=w_count
        for i in range(k,len(blocks)):
            if blocks[i]=='W':
                w_count+=1
            if blocks[i-k]=='W':
                w_count-=1
            white=min(w_count,white)
        return white

        