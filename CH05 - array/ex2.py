# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:41:33 2020

@author: madar
"""
def dutch_flag(A,indx:int):
    S = A[indx]
    small,big=0,len(A)-1
    #for moving both equal and bigs
    while small != big:
        if A[small]<S:
            small+=1
        else:
            A[small],A[big] = A[big],A[small]
            big-=1
    new_small,new_big =small,len(A)-1
    #for moving only bigs
    while new_small != new_big:
        if A[new_small]==S:
            new_small+=1
        else:
            A[new_small],A[new_big] = A[new_big],A[new_small]
            new_big-=1
    
    return A
#%%
#example
print(dutch_flag([2,3,1,8,6,7,6,4,5,2,9,4,4,5,4,7,4],7))