class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, each in enumerate(zip(*strs)):
            if len(set(each)) >1:
                return strs[0][:i]
        
        return min(strs)
