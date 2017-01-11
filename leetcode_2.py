# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        rListNode=ListNode(0)
        tmpNode1=l1
        tmp_numlist1=[]
        tmp_num1=0
        tmpNode2=l2
        tmp_numlist2=[]
        tmp_num2=0
        while True:
            tmp_numlist1.append(tmpNode1.val)
            if tmpNode1.next is not None:
                tmpNode1 = tmpNode1.next
            else:
                break
        
        len_tmp = len(tmp_numlist1)
        
        for i in range(1,len_tmp+1):
            tmp_num1+=tmp_numlist1.pop()*(10**(len_tmp-i))
        
        while True:
            tmp_numlist2.append(tmpNode2.val)
            if tmpNode2.next is not None:
                tmpNode2 = tmpNode2.next
            else:
                break
        
        len_tmp = len(tmp_numlist2)
        
        for i in range(1,len_tmp+1):
            tmp_num2+=tmp_numlist2.pop()*(10**(len_tmp-i))
        
        sum = tmp_num1 + tmp_num2
        
        count = 1
        level = 0
        while True:
            count=count*10
            level+=1
            if sum<=count:
                break
            
        rtmpNode = rListNode
        if sum==count:
            rtmpNode.val=0
            while count!=1:
                if count == 10:
                    rtmpNode.next = ListNode(1)
                    count /= 10
                else:
                    tmpNode=ListNode(0)
                    rtmpNode.next=tmpNode
                    rtmpNode=rtmpNode.next
                    count /= 10
            return rListNode
        else:
            tmpList=[]
            while count!=1:
                count/=10
                tmpList.append(sum/(count))
                sum%=count
                
            rtmpNode.val = tmpList.pop()    
            while level and tmpList:
                tmpNode=ListNode(tmpList.pop())
                rtmpNode.next=tmpNode
                rtmpNode=rtmpNode.next
                level-=1
            return rListNode
