#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#    Author :  Daydup
#    E-mail :  hainuzsr@gmail.com
#    Date   :  161228 19:19:06
##################################
#9.Palindrome Number
##################################

#注意：负数不能是回文数

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tmp=[]
        if x<0 :
            return False
        if x<10:
            return True
        while True:
            tmp.append(x%10)
            x=x/10
            if x<10:
                tmp.append(x)
                break
        for i in range(len(tmp)/2):
            if tmp[i]!=tmp[-1-i]:
                return False
        return True
