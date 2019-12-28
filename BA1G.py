
# coding: utf-8

# In[22]:


"""
난이도 : 2

문제 : 두 서열이 주어지고, 차이가 나는 염기가 몇개인지 출력하시오.
    (두 서열에 대해 차이나는 염기 개수는 hamming distance라고 한다.)
    
알고리즘 : 두 서열에 대해 길이가 같다는 가정하에,
    for문을 돌며 인덱스를 이용해 서로 다른 염기일 때 마다 score에 +1해서 차이나는 염기개수 구함."""
def print_score(file):
    s1,s2 = file.read().rstrip().split('\n')
    score=0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            score+=1
    print(score)
    return None

with open('rosalind_ba1g.txt','r') as file:
    print_score(file)

