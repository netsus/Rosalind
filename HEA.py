# coding: utf-8
"""
난이도 : 3

문제 : 

알고리즘 : 
"""
from heapq import heappop, heappush, heapify

def Max_Heap(num_li):
    heap = []
    heapify(heap)
    result_li = []
    for n in num_li:
        heappush(heap, -1 * n)
    for i in heap:
        result_li.append(str(-1 * i))
    return result_li

with open('rosalind_hea.txt') as f:
    n = int(f.readline())
    num_li = list(map(int,f.readline().split()))
    result_li = Max_Heap(num_li)
    
with open('rosalind_hea_answer.txt','w') as fo:
    result = ' '.join(result_li)
    fo.write(result)