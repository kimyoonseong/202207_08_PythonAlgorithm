import sys
sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,



n,m=map(int,input().split()) 
a=list(map(int,input().split()))
a.sort()
'''
for i in range(n):
    
    if a[i]==m:
        print(i+1)    
'''
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1
        
