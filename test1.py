#coding=utf-8
'''
for i in range(1,5):
    for j in range(1,5):
        for k in  range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                print i,j,k
'''


s=[(x,y,z) for x in range(1,5) for y in range(1,5) for z in range(1,5) if(x!=y)and(x!=z)and(y!=z)]
for x in s:
    print x