
# coding: utf-8

# In[133]:


"""
난이도 : 3

문제 : 각각 정렬된 배열에 대해, 배열A의 길이와 배열A, 배열B의 길이와 배열B를 순차적으로 줄바꿔 주어짐.
    배열A와 배열B를 합병 정렬하시오.

알고리즘 : 주어진 입력에 대해 배열을 나누어 반환하는 함수 make_arr를 통해 arrA와 arrB를 반환 (각각 배열A와 배열B)
    merge_sort함수는 arrA와 arrB를 입력받아 재귀적으로 정렬하며 출력하는 함수
    (RecursionError: maximum recursion depth exceeded in comparison -> 재귀 스택 메모리 초과 에러뜸)
    -> 그냥 arrA와 arrB를 합치고 sorted 함수 이용
    
"""

def make_arr(file):
    pre_li = file.read().rstrip().split('\n')
#     n, m = map(int,pre_li[::2])
    arrA , arrB = [list(map(int,seq.split())) for seq in pre_li[1::2]]
    return arrA, arrB

def merge_sort(arrA,arrB):
    if len(arrA) == 0:
        print(*arrB)
    elif len(arrB) == 0:
        print(*arrA)
    elif arrA[0] < arrB[0]:
        print(arrA[0],end=' ')
        merge_sort(arrA[1:],arrB)
    else:
        print(arrB[0],end=' ')
        merge_sort(arrA,arrB[1:])

with open('rosalind_mer.txt','r') as file:
    arrA , arrB = make_arr(file)
#     merge_sort(arrA,arrB)
with open('OUT.txt', 'w') as outFile:
    print(*sorted(arrA+arrB), file=outFile)   
    

