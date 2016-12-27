#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#    Author :  Daydup
#    E-mail :  hainuzsr@gmail.com
#    Date   :  161226 19:38:18
##################################
#6.ZigZag Conversion
##################################

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length_s=len(s)
        if numRows==1 or numRows>=length_s:
            return s
        tmpList = ['']*numRows
        index, step = 0, 1
        for x in s:
            tmpList[index]+=x
            if index == 0:
                step = 1
            elif index == numRows-1:
                step =-1
            index += step
        
        return ''.join(tmpList)
            

s=Solution()
print (s.convert('abcdefghijk',4)) 
