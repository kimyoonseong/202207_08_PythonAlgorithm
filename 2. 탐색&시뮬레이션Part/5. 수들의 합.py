import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,


a,b=map(int,input().split())
k=list(map(int,input().split()))
'''
cnt=0
res=0
for i in k:
    res+=i  
    if i==b:
        cnt+=1
        res=0
    elif res==b:
        cnt+=1
        res=i       
    elif res>b:
        res=0
    #print(res)
    #print(cnt)

    
print(cnt) #20점..
'''
lt=0
rt=1
tot=k[0]
cnt=0
while True:
    if tot<b:
        if rt<a:
            tot+=k[rt]
            rt+=1
        else:
            break
    elif tot==b:
        cnt+=1
        tot-=k[lt]
        lt+=1
    else:
        tot-=k[lt]
        lt+=1
print(cnt)
