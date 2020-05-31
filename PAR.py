# coding: utf-8
"""
난이도 : 1.5

문제 : 정수(n)과 n개의 수로 이루어진 배열이 행 구분자로 주어진다.
n 개로 이루어진 배열에서 첫번째 원소(first)를 기준으로, 
first 보다 작은 수들은 앞부분에, first 보다 큰 수들은 뒷부분에 배치하여 출력하시오.
(first보다 작은 수와 first보다 큰 수는 따로 정렬할 필요 없다.)

알고리즘 : par함수는 n개로 이루어진 배열을 li에 저장하고 첫 번째 원소를 first에 저장한다.
for문을 통해 li를 차례로 반복하면서,
    first보다 작으면 front_li에 저장,
    first보다 크면 enc_li에 저장,
    first와 같은 경우(else:) 패스
    front_li와 first, end_li를 차례로 붙여서 (리스트의 덧셈) result 리스트 생성
    result 리스트를 공백 구분자로 출력하면 정답이 된다.
"""
def par(li):
    first=li[0]
    front_li=[]
    end_li=[]
    for num in li:
        if num < first:
            front_li.append(num)
        elif num > first:
            end_li.append(num)
        else:
            pass
    result = front_li + [first] + end_li
    return result

with open('../dataset/rosalind_par.txt') as f:
    n=int(f.readline())
    li=list(map(int,f.readline().split()))

with open('../result/rosalind_par_result.txt','w') as fo:
    result = par(li)
    fo.write(' '.join(list(map(str,result))))