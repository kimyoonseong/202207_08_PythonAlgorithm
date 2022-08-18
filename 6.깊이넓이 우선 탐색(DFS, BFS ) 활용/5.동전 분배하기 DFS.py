import sys
#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,
def DFS(L):
    global res
    
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()#중복을 허락하지 않는
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha         # 세사람의 총액이 달라야함으로 SET중복되면 TMP의 LEN이 2가
    else:
         for i in range(3):
             money[i]+=coin[L]
             DFS(L+1)
             money[i]-=coin[L]
            

if __name__=="__main__":
    n=int(input())
    coin=[]
    tmp=[]
    money=[0]*3
    res=2147000000
    for _ in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)
