import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

N,M=map(int,input().split())
a=list(map(int,input().split()))


a.sort()

Sum=0
cnt=0
while a:
    if len(a)==1:
        cnt+=1
        break#한명 태우고 break
    
    if a[0]+a[-1]>M:# 이 두개만하면 마지막 하나 남았을때 모순이생김 a[0]=a[-1]
        cnt+=1
        
        a.pop()
    elif a[-1]+a[0]<=M:
        a.pop()
        a.pop(0)
        cnt+=1
     
    
print(cnt)
