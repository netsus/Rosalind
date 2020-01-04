
# coding: utf-8

# In[161]:


"""
난이도 : 2.4

문제 : FASTA 형식으로 RNA 서열이 하나 주어진다. (최대 80bp)
    RNA 서열은 A와 U의 개수가 같고, G와 C의 개수가 같다.
    해당 서열을 둥글게 말아 그래프로 만들때, A와U G와C가 모두 연결되는 완전 그래프의 경우의수는 몇개인가?
    

알고리즘 : A와 U의 개수가 같고, G와 C의 개수가 같다. 그러므로, AU쌍과 GC 쌍은 항상 짝수개이다.
    A-U , G-C 가 모두 연결되는 경우의 수는 (A와 U가 연결되는 경우의수) * (G와 C가 연결되는 경우의수) 이다.
        A가 U중 하나를 선택하고, 남은 A가 남은 U중 하나를 선택하고 ...
        이는 A 개수 * A개수-1 * ... 과 마찬가지이다. 즉, (A 개수)! 이다.
    그러므로 최종 결과는 (AU쌍 개수)! * (GC쌍 개수)! 이다.
"""
from math import factorial

with open('rosalind_pmch.txt') as file:
    # make input
    id = file.readline().rstrip()[1:]
    seq=''
    for line in file:
        seq += line.rstrip()
    # total possible number
    AU_pair_num = seq.count('A')
    GC_pair_num = seq.count('G')
    print(factorial(AU_pair_num)*factorial(GC_pair_num))

