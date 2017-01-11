class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        Seq = A
        sumA = sum(Seq)
        len_A = len(Seq)
        maximum = 0
        
        for i in range(len_A):
            maximum += i*Seq[i]
        tmp=maximum
        for i in range(len_A-1, 0 ,-1):
            tmp += (sumA - Seq[i]*len_A)
            maximum = max(maximum, tmp)
        return maximum

