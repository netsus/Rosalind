
# coding: utf-8

# In[209]:


'''
문제 1항과 2항은 1이다.피보나치 수열에서 n 번째 항은 ?
알고리즘 : 2번째항 이하는 모두 1, 그외는 앞의 두항을 합한값을 출력하는 fib 함수이용'''

def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(int(input())))

