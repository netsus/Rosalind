
# coding: utf-8

# In[185]:


"""
난이도 : 2.5

문제 : 주어진 DNA 서열에 대해 reverse하고 상보적인 DNA 서열을 출력하시오

알고리즘 : 주어진 DNA 서열을 뒤집고, A는 T로 T는 A로 G는 C로 C는 G로 그외의 염기가 있다면 에러출력하는 함수 Reverse_Complement 이용
    모두 바꿔 출력.

"""

def Reverse_Complement(file):
    seq=file.read().rstrip()
    reverse_seq = seq[::-1]
    comple_seq=''
    for base in reverse_seq:
        if base=='A':
            comple_seq+='T'
        elif base=='T':
            comple_seq+='A'
        elif base=='G':
            comple_seq+='C'
        elif base=='C':
            comple_seq+='G'
        else:
            raise "Error"
    return comple_seq

with open('rosalind_ba1c.txt','r') as file:
    print(Reverse_Complement(file))

