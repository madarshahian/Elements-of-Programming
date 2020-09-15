data = [2,4,1,5,7,8,23,5,77,8,0,1,23,4]
def even_odd(data:list)->list:
    j=0
    for i in range(len(data)):
        if data[i]%2==0:
            data[j],data[i]=data[i],data[j]
            j+=1
    return data


def even_odd_2(data:list)->list:
    next_even,next_odd = 0,len(data)-1
    n = 0
    while next_even<next_odd:
        n+=1
        if data[next_even] % 2 == 0:
            next_even+=1
        else:
            data[next_even],data[next_odd]=data[next_odd],data[next_even]
            next_odd-=1
    return data,n
            
