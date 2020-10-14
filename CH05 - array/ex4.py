# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 18:41:33 2020
"""
List1 = [8,5,9,4,5,3,0,8]
List2 = [1,4,7,8,9]


            
        
def Multiply(List1,List2):
    List1 = [0]+List1
    a=0
    Res_final = [0]*len(List1)
    
    for j in reversed(range(len(List2))):
        A = List2[j]
        c=0
        Res = [0]*len(List1)
        for i in reversed(range(len(List1))):
            
            m=(List1[i]*A+a)%10
            a=(List1[i]*A+a)//10
            Res[i] = m            
            if Res_final[i]+m+c<=9:
                Res_final[i]+=m+c
                c=0
            else:
                Res_final[i]=(Res_final[i]+m+c)%10
                c=1
        Res_final = [0]+Res_final
    if Res_final[0] == 0:
        Res_final = Res_final[1:]
    return Res_final
        
        
    

    
#%%
#example
print(Multiply(List1,List2))