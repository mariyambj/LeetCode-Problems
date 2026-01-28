class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left=0
        result=[]
        count={}
        for right in range(9,len(s)):
            curr=s[left:right+1]
            if curr not in count:
                count[curr]=1
            else:
                if count[curr]==1:
                    result.append(curr[:])
                    count[curr]+=1
            left+=1
        return result
        '''sub_string=[]
        result=[]
        for right in range(len(s)-9):
            sub_string.append(s[right:right+10])
        for i in range(len(sub_string)):
            for j in range(i+1,len(sub_string)):
                if sub_string[i]==sub_string[j]:
                    if sub_string[i] not in result:
                        result.append(sub_string[i])
        return result'''

'''        left=0
        sub_strings=[]
        substring=""
        for right in range(len(s)):
            substring+=(s[right])
            sub_strings.append(s[left:right+1])
        for i in range(len(sub_strings)):
            for j in range(len(sub_strings)):
                if len(s[i])==10 and len(s[j])==10:
                    if s[i]==s[j]:
                        return s[i],s[j]'''
        
            
        