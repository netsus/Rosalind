
# coding: utf-8

# In[210]:


"""
난이도 : 3

문제 : 처음에 토끼 1마리존재, 태어난 토끼는 2개월 후에 첫 새끼를 낳음.
    토끼의 수명이 m개월 일때, n 개월 후에 토끼의 개체수는??
    
알고리즘 : rabbit_li의 길이를 m으로함. 0번째는 막태어난 토끼 개체수, 1번째는 1개월된 토끼 개체수 ...
tmp_li를 이용해 1개월 단위로 계산해줌

1개월에 일어나는 일 : 0개월된 토끼는 1개월된 토끼로 이동, m-1개월된 토끼는 그 수 만큼 새끼토끼를 낳고 죽음.
    0 초과, m-1 미만 개월된 토끼는 그 개체수만큼 새끼토끼를 낳고, 모두 1개월 성장
    
처음에 1개월은 새끼토끼 1마리존재하기 때문에 for문 n-1번 반복. 
rabbit_li에 tmp_li를 얕은 복사해야 rabbit-li 수정과 tmp_li 수정이 개별적으로 일어날 수 있음

단, 토끼의 수명이 1개월일땐 새끼토끼가 새끼를 낳지 못하고 죽기때문에 개체수가 0인것을 별도처리해줌
"""

f = open('rosalind_fibd.txt','r')
n,m = map(int,f.read().rstrip().split())

def mortal_fib(n,m):
    rabbit_li=[]
    tmp_li=[]
    for i in range(m):
        rabbit_li.append(0)
        tmp_li.append(0)
    rabbit_li[0]=1
    if m==1:
        return 0
    else:
        for _ in range(n-1):
            if rabbit_li[0]==0:
                pass
            else:
                tmp_li[1]=rabbit_li[0]
            tmp_li[0]=rabbit_li[len(rabbit_li)-1]
            for i in range(1,len(rabbit_li)-1):
                tmp_li[0]+=rabbit_li[i]
                tmp_li[i+1]=rabbit_li[i]
            rabbit_li=tmp_li[:] # shallow copy
            for i in range(len(tmp_li)): # initialize tmp_li
                tmp_li[i]-=tmp_li[i]
    return sum(rabbit_li)

mortal_fib(n,m)

