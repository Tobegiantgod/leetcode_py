class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        tmpList = []
        i=0
        j=1
        while True:
            if j==len(s)-1:
                if maxlen < j-i:
                    maxlen = j-i
                break    
            if s[i] == s[j]:
                if maxlen < j-i:
                    maxlen = j-i
                i+=1
                j+=1
            else:
                j+=1
        return maxlen
            
