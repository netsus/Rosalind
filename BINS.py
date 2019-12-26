
# coding: utf-8

# In[229]:


'''
문제 : 입력받은 위의 두숫자는 아래 두배열의 길이
첫번째 배열은 정렬된 배열, 두번째 배열은 정렬되지 않은배열.
정렬되지 않은 배열을 순차적으로 돌며 원소가 정렬된 배열의 몇번째에 있는지 출력하고, 없으면 -1 출력
알고리즘 : 정렬된 배열과 정렬되지 않은 배열만 사용하여, 정렬되지 않은 배열을 for문으로 돌며 정렬된 배열에서의 index+1 출력
예외처리를 일으켜, 없을땐 -1 출력'''

f = open('rosalind_bins.txt','r')
fs = f.read()
fl = fs.rstrip().split('\n')

sort_list=fl[2].split()
unsort_list=fl[3].split()

for i in unsort_list:
    try:
        print(sort_list.index(i)+1,end=' ')
    except:
        print(-1,end=' ')

