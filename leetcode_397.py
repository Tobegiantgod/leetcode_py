class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        print ('Input:\n%d'%n)
        
        count = 0
        tmp=n
        while tmp!=1:
            if tmp==3:
                count += 2
                break
            if tmp%2==0:
                tmp=tmp/2
            else:
                tmp1=(tmp+1)
                tmp2=(tmp-1)
                if (tmp1/2)%2==0 and (tmp2/2)%2==1:
                    tmp=tmp1
                else:
                    tmp=tmp2
            
            count+=1    
        return count
