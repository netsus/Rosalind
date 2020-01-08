
# coding: utf-8

# In[44]:


"""
난이도 : 2

문제 : 정렬된 문자가 10개 이하로 주어진다. 그리고 10이하의 정수 n이 주어진다.
    정렬된 문자 순서대로 n개의 중복순열 모든 경우의수를 출력하시오
    
알고리즘 : itertools 라이브러리의 product는 중복순열을 출력하는 함수이다. 
    product(콜렉션, repeat= 뽑을 개수) 하면 콜렉션에서 뽑을 개수만큼 순차적으로 출력해 준다.
    이를 이용하여 print_product 함수를 만들고 출력 포맷에 맞게 출력해준다.
"""
from itertools import product

def print_product(ordered_collection, n):
    for string in product(ordered_collection,repeat=n):
        print(''.join(string))

with open('rosalind_lexf.txt') as file:
    # make input
    ordered_collection = file.readline().rstrip().split()
    n = int(file.readline().rstrip())
    # use function
    print_product(ordered_collection, n)

