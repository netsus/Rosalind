
# coding: utf-8

# In[155]:


"""
난이도 : 3

문제 : 서열(seq)과 정수k가 주어진다. 
    'ACGT'에 대해 중복순열로 k길이의 kmer를 순서로 하여, 서열(seq)에 kmer가 존재하면 그 개수를, 없으면 0을 출력한다.

알고리즘 : make_kmer_li 함수는 seq과 k를 입력받아 가능한 kmer의 리스트를 반환한다.
    print_kmer_in_kmer_li함수는 seq, k, kmer_li를 입력받아 
    for문을 돌면서 'ACGT' 내에서 k길이의 중복순열을 순차적으로 탐색하며
        k길이의 중복순열을 kmer에 저장        
        kmer가 seq에 존재한다면, kmer_li에 몇개존재하는지 counter[kmer]에 저장
        kmer가 seq에 존재하지 않으면, 0으로 초기화
    counter의 values들을 출력 포맷에 맞게 출력

"""

from collections import Counter
from itertools import product

def make_kmer_li(seq,k):
    kmer_li=[]
    for i in range(len(seq) - k + 1):
        kmer = seq[i: i+k]
        kmer_li.append(kmer)
    return kmer_li

def print_kmer_in_kmer_li(seq,k,kmer_li):
    counter = Counter()
    for i in product('ACGT',repeat=k):
        kmer = ''.join(i)
        if kmer in seq:
            counter[kmer] = kmer_li.count(kmer)
        elif counter[kmer] == 0:
            counter[kmer] = 0
    for i in counter.values():
        print(i, end=' ')

with open('rosalind_ba1k.txt') as file:
    # make input
    seq = file.readline().rstrip()
    k = int(file.readline().rstrip())
    # use function
    kmer_li = make_kmer_li(seq,k)
    print_kmer_in_kmer_li(seq,k,kmer_li)

