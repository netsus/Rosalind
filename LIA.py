
# coding: utf-8

# In[10]:


"""
난이도 : 5 (확률에 대한 지식이 확실하다면 쉬울듯, 없으면 이리저리 해봐야 한다.)

문제 : 정수 k, N이 주어진다. 처음에 1명의 Aa Bb인 사람이 있고, 항상 Aa Bb와 짝지어 2명의 자식을 낳는다. (A와 B는 독립)
    처음에 1명은 0번째 세대이고, 2명은 1번째 세대 ...
    문제는 k 번째 세대에서 Aa Bb 형질을 갖는 사람이 적어도 N명 이상일 확률을 구하는 것이다.

알고리즘 : 적어도 N 명 이상일 확률이라는 것은 Aa Bb가 0명일 확률 부터 N-1일 확률까지를 모두 더한것을 1에서 뺀값을 의미한다.
    예를들어, 적어도 1명 이상일 확률은 1 - (한 명도 없을 확률)
    이때 1에서 뺄 확률값들에는 조합(Combination)이 필요하다.
    예를들어, N이 2일때, 1 - (한 명도 없을 확률 + 1명만 있을 확률)인데,
        한 명도 없을 확률 = Combination(kst,0) * (1/4)^0 * (3/4)^kst 이다. 
            (kst는 2의 k승으로 k번째 세대의 개체수, 1/4은 AaBb가 나올 확률인데 독립적으로 항상 일정하다. 3/4은 AaBb가 나오지 않을 확률)
        1명만 있을 확률 = Combination(kst,1) * (1/4)^1 * (3/4)^(kst-1)
            즉, K번째 세대중에서 1명이 AaBb일 확률(1/4) 이고 나머지(kst-1)은 AaBb가 아닐 확률 3/4^(kst-1)이다.
            
    이를 통해, k와 N이 주어지면 k번째 세대에서 AaBb가 적어도 N명 이상일 확률을 구할 수 있다.
"""

def nChoosek(n,k):
    nomi = 1
    denomi = 1
    k = min(k,n-k) # 빠른 계산을 위해 최소값 찾기
    for i in range(1,k+1):
        denomi *= i
        nomi *= n+1-i
    return nomi//denomi

def at_least_n_in_kst(file):
    k,n = map(int,file.read().rstrip().split())
    kst = 2**k
    exception=0
    for i in range(n):
        exception += nChoosek(kst,i) * ((1/4)**i) * ((3/4)**(kst-i))
    print(1-exception)

with open('rosalind_lia.txt','r') as file:
    at_least_n_in_kst(file)

