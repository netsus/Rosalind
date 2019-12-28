
# coding: utf-8

# In[8]:


"""
난이도 : 2

문제 : DNA 서열이 주어지는데, C염기가 나오면 -1, G염기가 나오면 +1 나머진 유지 하여 score_list를 생성한다.
    C나 G가 나오면 -1과 +1의점수가 다음 인덱스에서 적용되는 점을 주의!

알고리즘 : 주어진 서열에대해 score_list를 생성한다 -> score_li (함수 make_score_li 이용)
    생성된 score_li를 입력으로 하여, 최소 값에 대한 인덱스를 출력한다. (함수 print_min_num_index 이용)

"""
def make_score_li(file):
    seq = file.read().rstrip()
    score=0;score_li=[]
    for i in seq:
        score_li.append(score)
        if i=='C':
            score-=1
        elif i=='G':
            score+=1
    score_li.append(score)
    return score_li

def print_min_num_index(score_li):
    Min_num = score_li.count(min(score_li))
    idx = -1
    for i in range(Min_num):
        idx = score_li.index(min(score_li),idx+1)
        print(idx,end=' ')
    return None

with open('rosalind_ba1f.txt','r') as file:
    score_li = make_score_li(file)
    print_min_num_index(score_li)

