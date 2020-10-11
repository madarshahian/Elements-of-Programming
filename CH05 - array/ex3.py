# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:41:33 2020
"""
List = [9,5,3,9,9,9]


            
        
def plusone(List):
    status = True
    i=-1      
    while status:
        if List[i] == 9:
            List[i] = 0
            if i!=-len(List):
                i-=1
            else:
                List = [1]+List
                status = False
        else:
            List[i] = List[i]+1
            status = False
    return List
    
#%%
#example
print(plusone(List))