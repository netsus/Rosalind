
# coding: utf-8

# In[154]:


"""
난이도 : 3

문제 : 정수 인덱스(idx)와 k가 주어진다.
    idx는 서열에 대한 4진수를 10진수로 변환한 값이고, k는 서열의 개수이다.

알고리즘 : 주어진 idx를 이진수로 바꾼뒤 2개씩 잘라 bin_li 리스트에 넣는다 (2진수를 2개씩 자르면 각각 4진수이기 때문)
    for문으로 bin_list를 순차적으로 탐색하며
        4진수로 변환하고, 그 값을 염기서열로 바꿔 seq에 문자열로 하나씩 추가한다.
        이때, 이진수가 홀수개이면 4진수로바꿀때 값 1개는 한자리 2진수이기 때문에 뒤에 0을 붙여서 4진수로 만들어준다.
    A는 4진수로 0이기 때문에 이론상 4진수끝에 아무리 붙어도 수자체에는 변함이 없다.
    그래서 내가 구한 서열 길이 len(seq)과 주어진 서열 길이 k 의 차이만큼 A를 붙여줘야 한다.
"""
    


def NumberToPattern(idx,k):
    
    score_di = {'A':0,'C':1,'G':2,'T':3}
    reverse_score_di = dict((v,k) for k,v in score_di.items())
    
    binary = bin(idx)[2:][::-1]
    bin_li = [binary[i:i+2] for i in range(0,len(binary),2)]
    seq=''
    for bi in bin_li:
        if len(bi) == 1:
            bi += '0'
        quater = int(bi[0]) + int(bi[1])*2
        seq += reverse_score_di[quater]
    print((k-len(seq))*'A'+seq[::-1])

with open('rosalind_ba1m.txt') as file:
    idx, k = map(int,file.read().rstrip().split('\n'))
    NumberToPattern(idx,k)

