#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#    Author :  Daydup
#    E-mail :  hainuzsr@gmail.com
#    Date   :  170107 10:56:26
##################################
#21.Merge Two Sorted Lists
##################################
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is not None:
            return l2
        if l2 is None and l1 is not None:
            return l1
        if not l1 and not l2:
            return None
        
        rListNode = ListNode()
        tmp = rListNode
        while l1 or l2:

            if l1.val <= l2.val:
                tmp.val = l1.val
                l1 = l1.next            
            else:
                tmp.val = l2.val
                l2 = l2.next
            if l1 is None:
                tmp.next = l2
                return rListNode
            if l2 is None:
                tmp.next = l1
                return rListNode
            tmp.next = ListNode()
            tmp = tmp.next
