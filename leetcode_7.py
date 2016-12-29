#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#    Author :  Daydup
#    E-mail :  hainuzsr@gmail.com
#    Date   :  161229 20:31:54
##################################
#7.Reverse Integer
##################################
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if -10<x<10:
            return x
        flag=1
        if x<=-10:
            x=-x
            flag=0
        rx=0
        numstr=str(x)
        len_num=len(numstr)
        for i in range(len_num):
            rx += (x%10)*10**(len_num-1-i)
            x/=10
        if rx>2147483647:
            return 0
        if flag==0:
            return -rx
        return rx


#test
so=Solution()
print so.reverse(-2342356)

