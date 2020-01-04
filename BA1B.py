
# coding: utf-8

# In[114]:


"""
난이도 : 1.7

문제 : 서열과 k 값을 입력받는다.
        서열내에서 k길이를 갖는 서열중 가장 많이 반복되는 서열을 출력하시오.
        가장 많이 반복된게 여러개의 서열이면 그 서열들을 순서에 상관없이 출력.

알고리즘 : 서열을 seq에 저장, k를 k에 저장
    for문을 돌며 서열에 대해 k길이만큼씩 순차적으로 탐색하며 딕셔너리(k_mer_dict)에 저장
        순차적으로 탐색하는 k 길이의 서열을 k_mer에 저장하고
        k_mer가 k_mer_dict에 존재하면 갯수 1 더해주고,
        존재하지 않으면 1로 초기화
    
    가장 많이 반복된 횟수인 max(k_mer_dict.values())를 most_freq에 저장
    k_mer_dict에서 most_freq만큼 반복된 서열(key)값을 모두 출력 (순서 상관 없음)
"""

def print_most_freq_kmer(file):
    seq , k = file.read().rstrip().split('\n')
    k=int(k)

    k_mer_dict=dict()

    for i in range(0,len(seq)-k+1):
        k_mer = seq[i:i+k]
        if k_mer in k_mer_dict:
            k_mer_dict[k_mer]+=1
        else:
            k_mer_dict[k_mer]=1

    most_freq = max(k_mer_dict.values())

    for key,val in k_mer_dict.items():
        if val == most_freq:
            print(key,end=' ')
    return None

file = open('rosalind_ba1b.txt','r')
print_most_freq_kmer(file)

