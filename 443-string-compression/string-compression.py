class Solution:
    def compress(self, chars: List[str]) -> int:
        read=write=0
        while read<len(chars):
            cur_char=chars[read]
            count=0
            while read<len(chars) and chars[read]==cur_char:
                read+=1
                count+=1
            chars[write]=cur_char
            write+=1
            if count>1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        return write
        