
# coding: utf-8

# In[62]:


"""
난이도 : 2

SUBS 문제와 유사

문제 : total_seq과 substring 두 서열을 입력받아, substring이 total_seq에 포함되는 부분이 몇개인지 출력

알고리즘 : total_seq에대해 처음부터 한칸씩 이동하며 substring 길이만큼 불러온다
불러온 seq이 substring과 같으면 cnt+=1
반복이 종료되면 cnt를 출력"""

def pattern_count(file):
    total_seq , substring =  file.read().rstrip().split('\n')
    c = len(total_seq) - len(substring) + 1
    cnt=0
    for i in range(c):
#         print(total_seq[i:i+len(substring)])
        if total_seq[i:i+len(substring)]==substring:
            cnt+=1
    return print(cnt)


file = open('rosalind_ba1a.txt','r')
pattern_count(file)

