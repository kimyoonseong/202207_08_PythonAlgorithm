import sys
sys.stdin=open("A.txt","r")

n=int(input())
a=list(map(int,input().split()))

ave=round(sum(a)/n)
min=21470000
for idx,x in enumerate(a): # idx 는 인덱스값 x은 실제 값
    tmp=abs(x-ave)# abs은 절댓값
    #print(tmp)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score: #값이 더 클때 !  주의) x>=score로 하면 앞번호가아닌 뒷번호가 된다
            #print(x)
            score=x
            res=idx+1
            #print(res)

print(ave, res)
