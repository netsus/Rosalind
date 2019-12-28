
# coding: utf-8

# In[105]:


"""
난이도 : 2.5
문제 : FASTA 포맷의 길이가 같은 두 서열을 입력받아 점 돌연변이의 일종인 치환 돌연변이 중에서
    퓨린(Purine: A, G)계열 안에서의 변이, 혹은 피리미딘(Pyrimidine: T, C)계열 안에서의 변이인 transition과 
    서로다른 계열간의 변이(치환)인 transversion에 대해
    transition / transversion 을 출력. (round함수를 이용해 소수점 11자리까지만 출력해봄)
    
알고리즘 : FASTA 포맷에 대해 서열만 리스트 형태로 만들어주는 make_seq_li 함수를 이용
    그 결과 만들어진 seq_li를 입력으로 받아 
    transition / transversion 을 계산하여 출력하는 transition_transversion_ratio함수 이용
 """

def make_seq_li(file):
    seq_li=[];idx=-1
    for line in file:
        line = line.rstrip()
        if line.startswith('>'):
            seq_li.append('')
            idx+=1
        else:
            seq_li[idx]+=line
    return seq_li

def transition_transversion_ratio(seq_li):
    s1, s2 = seq_li
    transition = 0 
    transversion = 0
    for i in range(len(s1)): # len(s1) == len(s2)
        if s1[i] != s2[i]:
            if (s1[i]+s2[i]) in ['AG','GA','CT','TC']:
                transition+=1
            else:
                transversion+=1
    return round(transition/transversion,11)

file = open('rosalind_tran.txt','r')
seq_li = make_seq_li(file)
print(transition_transversion_ratio(seq_li))

