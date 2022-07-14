import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,


a=[list(map(int, input().split())) for _ in range(7)]
cnt=0
for i in range(3):
    for j in range(7):
        tmp=a[j][i:i+5]
        if tmp==tmp[::-1]:# 회문검사
            cnt+=1
        for k in range(2):
            if a[i+k][j]!=a[i+5-k-1][j]:
                break;
        else:
            cnt+=1
print(cnt)    
