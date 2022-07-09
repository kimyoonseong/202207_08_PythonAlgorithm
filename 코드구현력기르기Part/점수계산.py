import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))

N=int(input())
a=list(map(int,input().split())) #이거는 [1,2,3,4,5]이런식
sum=0
res=0
for i in a:
    if i==1:
        res+=1
        sum+=res
    if i==0:
        res=0
print(sum)
    
