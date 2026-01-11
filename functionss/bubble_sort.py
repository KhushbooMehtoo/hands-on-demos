def matrixx(lst):
    
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            print(i,j)
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    
    return(lst)
        
print(matrixx([3,4,5,2,8,9,1,6,7]))