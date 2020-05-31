# coding: utf-8
"""
난이도 : 5

문제 : 20이하의 수(k)와 10,000이하의 수 n이 주어지고, 다음 줄부터 n개의 수로 이루어진 배열이 k개 주어진다. (행 구분자)

알고리즘 : k,n을 입력받고, num_li에는 k개의 배열이 이중 리스트로 모두 저장된다.
for문에서 k개의 배열을 반복하며
     각 배열을 li에 저장하고, Sum3함수를 호출한다.

    Sum3함수는 n개의 수로 이루어진 배열 1개를 입력받아,
    for문으로 n개의 수를 반복하며,
        found_dic에 Key로 '수'를, Value로 '수'의 인덱스 번호를 저장한다.(0번째 부터)
    found=False로 초기화한다.(found가 True가 된다는 것은 3개를 더해서 0이되는 세개의 짝을 찾았다는 의미.)
    for 문으로 리스트 개수(n개)만큼 반복하며, (0부터 n미만 -> a)
        first에 li의 a번째 값을 저장.
        또, for문으로 a+1부터 n 미만(-> b)을 반복하며
            second에 li의 b번째 값을 저장
            first와 second값을 더한 것에 -1 곱한 값이 found_dic의 키값에 존재한다면:
                세 값을 모두 더해 0이 된다는 의미이기 때문에, 각 인덱스에 1을 더해 출력.(파이썬은 인덱스가 0부터 시작인데, 문제는 1부터 시작이기 때문)
                found=True로 바꾸고 이중 포문을 빠져나가야 하기 때문에 break를 두 번 한다. (line41에서 한번 line31에서 한번)
                
    이중 포문을 모두 돌았는데도 세 값을 모두 더해 0이 되는 페어가 없으면 found는 False인 상태이며 -1이 출력된다.

"""
def Sum3(li):
    found_dic = {}
    for i in range(len(li)):
        found_dic[li[i]] = i
    found=False
    for a in range(len(li)):
        if found:
            break
        first = li[a]
        for b in range(a+1,len(li)):
            second = li[b]
            third = -1 * (first + second)
            if third in found_dic:
#                 print(f'In {li} => fisrt: {first}, second: {second}, third: {third}')
                c = found_dic[third]
                found=True
                print(f'{a+1} {b+1} {c+1}')
                break
    if found == False:
        print(-1)

with open('../dataset/rosalind_3sum.txt') as f:
    k,n = map(int,f.readline().split())
    num_li = list(map(lambda x: list(map(int,x.split())), f.read().rstrip().split('\n')))

for li in num_li:
    Sum3(li)