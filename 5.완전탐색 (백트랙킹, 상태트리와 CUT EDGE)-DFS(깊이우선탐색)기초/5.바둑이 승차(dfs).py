import sys

#sys.stdin=open("A.txt","r")
#n,m=map(int,input().split()) #정n면체 정m면
#a=list(map(int,input().split()))  #   1  3   5  띄어쓰기 받아옴.,

def DFS1():
    #cnt=3#지역변수
    print(cnt)#전역변수
    
def DFS2():
    global cnt #전역변수 지정!
    if cnt==5: 
        #cnt=cnt+1 지역변수 -> 에러 global cnt로 해결
        print(cnt)
        
if __name__=="__main__":
    cnt=5
    DFS1()
    DFS2()
    print(cnt)

def DFS():
    global a
    a=[7,8] #a= -> 로컬리스트를 만들겠다
    a=a+[4] # 로컬리스트임으로 에러가난다 =>global a 로 해결
    a[0]=7 #a[0]=   ->전역변수임으로 괜찮다
    print(a)
    
if __name__=="__main__":
    a=[1,2,3]
    DFS()
    print(a)
