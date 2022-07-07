import sys
#sys.stdin=open("A.txt","r")

n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

cnt=[0]*(n+m+3)

max=-21470000
'''
for i in range (1,n+1):
    for j in range(1,m+1):
        cnt[i+j]+=1
        print(cnt)

        
for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
        print(max)
for i in range(n+m+1):
    if max==cnt[i]:
        print(i,end=' ')

'''
a=[]
for num in range(1,n+1):
    for i in range (1,m+1):
        sum=num+i
        #print(int(sum))
        a.append(sum)
#print(type(a))
for i in  a:
    cnt[i]+=1
#print(cnt)
    
for i in range(n+m+1):
    if max<cnt[i]:
        max=cnt[i]
for i in range (n+m+1):
    if max==cnt[i]:
        print(i,end=' ')
    
