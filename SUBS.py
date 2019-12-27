
# coding: utf-8

# In[74]:


"""
문제 : total_seq과 substring 두 서열을 입력받아, substring이 total_seq에 포함되는 곳에 대해 시작 index를 출력.(시작index는 1)
알고리즘 : total_seq에대해 처음부터 한칸씩 이동하며 substring 길이만큼 불러온다
불러온 seq이 substring과 같으면 시작 인덱스를 index_li에 저장
반복이 종료되면 index_li를 출력"""

f = open('rosalind_subs.txt','r')
total_seq , substring =  f.read().rstrip().split('\n')

def subs(total_seq,substring):
    c = len(total_seq) - len(substring) + 1
    index_li=[]
    for i in range(c):
#         print(total_seq[i:i+len(substring)])
        if total_seq[i:i+len(substring)]==substring:
            index_li.append(i+1)
    return print(*index_li) # str(' '.join(map(str,index_li)))

subs(total_seq,substring)

