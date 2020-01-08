
# coding: utf-8

# In[55]:


"""
난이도 : 2

문제 : 정수 n과 k가 주어진다. 순열의 경우의 수에서 P(n,k)를 1,000,000으로 나눈 나머지를 출력하시오.

알고리즘 : permutation 함수는 ( n! / (n-k)! )을 계산한 것으로 n * (n-1) * ... * (n - k + 1) 을 계산한 것이다. 연산은 총 k번 이루어진다.
    결과 값을 total_num 에 저장하고 출력시에 1,000,000으로 나눈 나머지를 출력한다.
"""
def permutation(n,k):
    total_num = 1
    for num in range(k):
        total_num *= (n - num)
    print(total_num % 1000000)

with open('rosalind_pper.txt') as file:
    # make input
    n,k = map(int,file.readline().rstrip().split())
    # use function
    permutation(n,k)

