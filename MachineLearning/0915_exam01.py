# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:44:34 2023

@author: User
"""

import time

start = time.time()
sum=0

for i in range(1,100000001):
    sum=sum+i
    
end=time.time()

print('1+2+...+10000000=', sum)
print('소요시간은 ', end-start, '초입니다')

