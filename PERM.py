
# coding: utf-8

# In[143]:


"""
난이도 : 1.6

문제 : 7이하 자연수 n이 주어진다.
    1부터 n 까지 순열의 모든 경우의수 개수와, 모든 경우의수를 출력하시오.
    
알고리즘 : 모든 경우의수 개수는 factorial로 구한다. (math library의 factorial을 이용)
            (재귀를 이용해 직접 구현하려면 아래 fact함수처럼 구현할 수 있다.)
        모든 경우의 수는 itertools library의 permutations(순열)을 이용해 경우의수를 모두 출력한다.
"""

from itertools import permutations
from math import factorial

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

with open('rosalind_perm.txt') as file:
    n = int(file.readline().rstrip())
with open('rosalind_perm_out.txt','w') as outfile:
    print(factorial(n), file=outfile)
    for i in permutations(list(range(1,n+1))):
        print(*i, file=outfile)

