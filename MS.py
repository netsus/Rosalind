# coding: utf-8
"""
난이도 : 3.5

문제 : 정수(n)와 n개로 이루어진 수의 나열이 주어진다.
수를 Merge Sort로 정렬하여 출력하시오.

알고리즘 : Merge Sort를 구현해보는 것이다.
merge_sort함수에서는 재귀적으로 merge_sort를 호출하여 입력 리스트(li)를 반반씩 계속 나눈다. 재귀적 호출에서 li의 길이가 1이 되면(즉, 1개의 원소만 남은 리스트가 되면) li를 그대로 반환한다.
반반씩 계속 나누다 길이가 1이되면 그대로 반환하기 때문에, 
길이가 1이되어 반환 될 때마다(left_list가 길이 1의 리스트, right_list가 길이 1의 리스트)
merge 함수가 호출되게 된다.
merge 함수는 두 리스트(left_li, right_li)를 입력받아 
둘 중 하나라도 원소가 있으면, while 문을 돌며,
    left_li, right_li 둘다 원소가 있으면,
        두 리스트를 0번째 부터 비교해서 작은 수부터 result 리스트에 넣는다.
    둘 중 하나만 원소가 있으면,
        result 리스트에 원소가 있는 리스트를 붙여 준다.
while 문이 끝나면 result를 반환해준다.

전체 적인 과정은 반반씩 계속 나누다, 길이가 1이된 left_list 와 right_list에 대해 merge 함수에서 크기비교를 해서 정렬된 리스트인 result를 반환하며 다시 합쳐진다.
즉, merge_sort함수에서 반반씩 나뉘고, merge함수 에서 정렬이 이루어져 다시 두 배씩 합쳐지는 것이다.
"""

def merge_sort(li):
    if len(li)==1:
        return li
    mid = len(li)//2
    left_list = merge_sort(li[:mid])
    right_list = merge_sort(li[mid:])
    return merge(left_list,right_list)

def merge(left_li,right_li):
    result = []
    while len(left_li)>0 or len(right_li)>0:
        if len(left_li)>0 and len(right_li)>0:
            if left_li[0] > right_li[0]:
                result.append(right_li[0])
                right_li = right_li[1:]
            else:
                result.append(left_li[0])
                left_li = left_li[1:]
        elif len(left_li) > 0:
            result.extend(left_li)
            left_li=[]
        elif len(right_li) > 0:
            result.extend(right_li)
            right_li=[]
    return result

with open('rosalind_ms.txt') as f:
    n = int(f.readline())
    n_li = list(map(int,f.readline().rstrip().split()))

with open('rosalind_ms_result.txt','w') as fo:
    fo.write(' '.join(map(str,merge_sort(n_li))))