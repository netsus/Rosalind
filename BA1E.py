
# coding: utf-8

# In[50]:


"""
난이도 : 2.7

문제 : 서열과 k,L,t 가 주어진다.
    서열에 대해 L길이의 substring 내에서 k길이 만큼의 서열이 t 번 반복되는 모든 k-mer(k길이의 서열)를 출력하시오.

알고리즘 : 주어진 서열을 seq이라고 하고, seq 내에서 길이 L만큼을 모두 탐색한다. 
    for문을 이용하는데, len(seq) - L + 1 번 반복하면 한칸 씩 이동하며 모두 탐색한다. 이때 생성되는 길이L의 스트링을 substring이라 한다.
        한번 탐색할때마다 for문을 한번 더 사용하는데, substring에 대해서 k길이만큼씩 잘라내어, substring에 몇번 포함되는지 count 해준다.
        이때, count 결과가 t일때 k_mer_li에 추가시켜 준다.
    출력은 *set(k_mer_li)로 해주는데 이유는, k_mer_li에 중복이 많이 있을 수 있기 때문이다.
    
    이 알고리즘은 문제 그대로 직관적으로 짰지만, 매우 비효율 적이다. (개선 필요)
"""
def find_clump_kmer(file):
    pre_li = file.read().rstrip().split('\n')
    seq = pre_li[0]
    k,L,t = map(int,pre_li[1].split())
    
    k_mer_li=[]
    for i in range(len(seq) - L + 1):
        subseq = seq[i : i+L]
        for j in range(len(subseq) - k + 1):
            k_mer = subseq[j : j+k]
            if subseq.count(k_mer) == t:
                k_mer_li.append(k_mer) # 중복된 k_mer 들이 추가될 수 있다.
    print(*set(k_mer_li)) # 중복 제거

with open('rosalind_ba1e.txt') as file:
    find_clump_kmer(file)

