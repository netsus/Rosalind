
# coding: utf-8

# In[23]:


"""
난이도 : 2
문제 : 배열 길이와, 정렬되지 않은 배열을 공백을 구분자로 입력.
    해당 배열을 삽입 정렬하는데 몇번 swap이 일어나는지 출력.

알고리즘 : 실제로 주어진 pseudo code 를 그대로 구현하며 swap이 일어날때마다 cnt += 1
    insertion_sort 함수는 마지막에 cnt 반환하는 함수
    """
def insertion_sort(file):
    n , pre_li = file.read().rstrip().split('\n')
    n = int(n)
    li = list(map(int,pre_li.split()))

    cnt=0
    # 삽입 정렬 : for 문 한번 돌때마다 앞에 최소값이 하나씩 쌓여가며 정렬
    # 배열 뒷부분이 앞보다 크면 계속 앞으로 swap 한다.
    for i in range(1,n):
        k = i
        while k >= 1 and li[k] < li[k-1]:
            li[k] , li[k-1] = li[k-1], li[k]
            cnt+=1
            k-=1
    return cnt

file = open('rosalind_ins.txt','r')
print(insertion_sort(file))

