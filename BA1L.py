
# coding: utf-8

# In[95]:


"""
난이도 : 2

문제 : DNA 서열이 주어지면 4진수로 인식하여 수를 출력하시오.
    (A는 0, C는 1, G는 2, T는 3 으로 정함.)

알고리즘 : 주어진 서열을 seq에 저장하고, 
    PatternToNumber함수를 이용하여 점수(score)를 출력한다.
        seq[::-1]을 통해 반대로 뒤집어서 score_di를 이용해 점수를 추출하고 (4**자릿수)를 곱함으로써 4진수를 10진수로 변환한다.
        그렇게 변환된 모든 수를 더하여 출력한다.
"""
score_di = {'A':0,'C':1,'G':2,'T':3}

def PatternToNumber(seq):
    score = sum([score_di[seq[::-1][i]]*(4**i) for i in range(len(seq))])
    print(score)

with open('rosalind_ba1l.txt') as file:
    seq = file.readline().rstrip()
    PatternToNumber(seq)

