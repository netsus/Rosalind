
# coding: utf-8

# In[52]:


"""
난이도: 3.3 (라이브러리 복습 필요)

문제 : 첫줄에 배열개수, 배열원소개수 주어지고, 다음줄 부터
    배열이 공백을 구분자로 주어진다.
    각 배열에 대해 과반수 '초과'만큼 차지하는 배열 원소개수가 있으면 해당 배열원소 출력, 없으면 -1 출력
    
알고리즘 : 각 배열을 리스트 원소로 갖는 이중리스트인 array_list만듦.
    for문을 통해 array_list를 반복하며 각 배열에대해 Counter 함수를 통해 어떤 원소가 몇번 반복되는지 확인
    sorted함수에 operator.itemgeeter(1)인자를 주어서 값으로 정렬 (반복횟수로 정렬)
    가장 많이 반복된 원소와 그 반복횟수가 반환되면 그것이 n/2 초과이면 해당 원소 출력, 아니면 -1출력"""

from collections import Counter # 리스트의 원소 개수를 세어 딕셔너리로 만들어주는 라이브러리 -> Counter 함수
import operator # 딕셔너리의 값을 기반으로 정렬해주는 라이브러리 -> sorted 함수

def array_counter(file):
    file_list = file.read().rstrip().split('\n')

    k,n = map(int,file_list[0].split())

    array_list = [ list(map(int,i.split())) for i in file_list[1:] ]

    for array in array_list:
        arr_dic = Counter(array)
        key,cnt = sorted(arr_dic.items(),key=operator.itemgetter(1),reverse=1)[0]
        if cnt > n/2:
            print(key,end=' ')
        else:
            print(-1,end=' ')
    return None

file = open('rosalind_maj.txt','r')
array_counter(file)

