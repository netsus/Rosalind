# coding: utf-8
"""
난이도 : 3

문제 : 숫자의 개수(n)와 n개의 숫자 배열 (num_li)가 주어진다. num_li를 MAX HEAP(이진 완전 트리)으로 만든뒤, 이진 트리의 맨 위에서 아래로로, 왼쪽에서 오른쪽 순서로 차례대로 출력.(책 읽을 때 순서)
주어진 배열에 대해 MAX HEAP만 만족한다면 순서는 어떻게되든 상관 없다. (예시의 Sample Output을 보면 Sample Dataset에서 무작위로 Max Heap을 만들었음을 알 수 있다.)

알고리즘 : Max_Heap 함수에서 숫자의 배열을 max_heap으로 만든다. heapq의 기본은 min_heap 이기 때문에 heap에 넣을때 -1 을 곱해서 heappush를 해준다.
즉, 주어진 num_li에 -1을 곱해진 수로 min_heap을 만든 것.
min_heap을 완성하면, heap을 차례로 돌면서 다시 -1을 곱해서 result_li에 넣어준다. (min_heap을 순서대로 돌면 최소값 부터 나올텐데 -1을 곱하면 최대값이 된다.)

result_li를 공백 구분자로 출력하면 정답이 된다. (숫자가 너무 많아서 rosalind_hea_answer.txt로 정답 제출.)
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