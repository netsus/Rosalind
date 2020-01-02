
# coding: utf-8

# In[125]:


"""
난이도 : 5 (BA1N문제를 기반으로한 문제)

문제 : 서열(seq)과 정수 k,d가 주어진다.
    서열내에서 d개 이하의 미스매치로 최대한 많은 빈도로 존재하는 어떤 kmer를 출력하시오. (여러개일 수 있다.)

알고리즘 : list_below_d_mismatch 함수는 seq에 대해 d개 이하의 미스매치를 갖는 모든 서열(길이는 seq과 동일)을 반환

    most_frequent_kmer_below_d_mismatches 함수는 
    for문에서 seq에 대해 순차적으로 탐색하면서 k길이만큼의 subseq에 대해서
        list_below_d_mismatch 함수를 이용해 d개 이하의 미스매치를 갖는 모든 서열을 반환하며, counter에 서열과 반복된 숫자가 저장된다.
    
    counter 내에는 for문에서 생성된 모든 subseq에 대해 d개 이하 미스매치를 갖는 모든 서열과 탐색 횟수가 저장된다.
    탐색횟수는 곳 seq에서의 빈도이다. 그러므로 탐색횟수가 최대인 서열들을 모두 출력하면 된다.
"""
from collections import Counter

# about seq, below d mismatch same length
def list_below_d_mismatch(seq,d):
    if d == 0:
        return [seq]
    if len(seq) == 1 and d >= 1:
        return [base for base in 'ATGC']
    res=[]
    for base in 'ATGC':
        if seq[0] != base:
            res.extend( base + suffix for suffix in list_below_d_mismatch(seq[1:] , d-1) )
        else:
            res.extend( base + suffix for suffix in list_below_d_mismatch(seq[1:] , d) )
    return res        

def most_frequent_kmer_below_d_mismatches(seq,k,d): 
    counter = Counter()

    for i in range(len(seq) - k + 1):
        subseq = seq[i : i+k]
        for kmer in list_below_d_mismatch(subseq,d):
            counter[kmer] += 1

    maxCnt = max(counter.values())

    return [kmer for kmer in counter if counter[kmer] == maxCnt]

with open('rosalind_ba1i.txt') as file:
    seq = file.readline().rstrip()
    k,d = map(int,file.readline().rstrip().split())
    print( *most_frequent_kmer_below_d_mismatches(seq,k,d) )

