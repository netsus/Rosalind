
# coding: utf-8

# In[76]:


"""
난이도 : 4.9 (발상이 어려웠음.)

문제 : 공백을 구분자로 12글자 이하의 글자와 글자의 길이 n(4이하의 자연수)이 주어진다.
    주어진 글자만 사용하여, 한 글자 이상, n 글자 이하로 만들어지는 모든 글자를 
    주어진 글자 순서대로 출력하시오. ( D N A라고 주어지면 D가 N 앞이고, N은 A 앞 순서이다.)

알고리즘 : 먼저 주어진 글자를 공백 제거해서 sym에 저장하고, 자연수 n 을 변수 n에 저장한다.

    첫 번째 알고리즘: 함수 print_ordered_sym
    for 문을 돌며 1 이상, n이하의 자연수에 대해
        중복순열(product)를 이용하여 모든 1글자 부터, n 글자까지 모든 조합을 ordered_li에 저장한다.
    ordered_li를 정렬하는데 주어진 문자(sym)의 인덱스 값에 따라 정렬한다 (key 인자 이용)
    (key 인자에 람다를 이용하여 ordered_li의 각 원소(문자열)마다 처음에 주어진 문자(sym)에서의 인덱스를 바탕으로 정렬하면,
    sym 에서 앞에 오는 문자일 수록 인덱스값이 작아지기 때문에 주어진 문자에 대한 순서대로 정렬할 수 있다.)
    
    두 번째 알고리즘 : 함수 print_ordered_sym2    (다른 코드 참조. 발상이 좋다 -> 그리고 첫번째 알고리즘에 약 2배 빠르다)
    주어진 문자열(sym) 앞에 공백을 추가하여 변수 alphabet에 저장한다.
    for 문을 돌며 중복순열(alphabet,n) 값을 순차적으로 변수 x에 저장하며 반복한다.
        중복순열로 뽑힌 값(리스트)에서 각 원소를 모두 합쳐 문자열을 만들고 .strip()을 통해 앞과 뒤의 공백을 제거해 변수 xs에 저장한다.
        이때 공백으로 시작하지 않고(not x[0] == ' '), 내부에 공백이 포함되지 않는 문자열(not ' ' in xs)에 대해서만 출력한다.
        
        
    두 번째 알고리즘의 주된 발상은 주어진 문자열에 대해 공백을 맨 앞에 붙이고 이를 중복순열로 뽑았을 때 발생하는 상황이다.
        공백이 맨 앞에 있기 때문에 뽑힐 때 우선순위가 가장 높다고 볼 수 있다. (중복순열 함수인 product는 그냥 주어진 순서대로 뽑으니까)
        공백이 있음으로 해서 주어진 문자열에 대해 n개를 뽑을때 한글자 이상, n 글자 이하의 모든 경우의 수가 출력되는데
        공백으로 시작하지 않고, 문자 가운데 공백이 없는 것을 제외하고 출력하면,
        문제의 출력 순서와 정확히 일치하게 된다.
        
        이유는? 중복순열함수 product가 주어진 문자열에 대해 앞부터 순차적으로 뽑기 때문이다.
        즉, 공백을 우선순위가 빠른 하나의 문자로 취급함으로써, 
        1글자 이상, n글자 이하의 모든 경우의수를 출력할 수 있음과 동시에 주어진 문자 순서대로 출력도 가능한 것이다.

"""
from itertools import product


# 첫번째 알고리즘 : 10.7 ms ± 2.26 ms per loop (mean ± std. dev. of 20 runs, 100 loops each)
def print_ordered_sym(sym,n):
    ordered_li = []
    for i in range(1,n + 1):
        ordered_li += ([''.join(sym) for sym in product(sym,repeat=i)])
    return sorted(ordered_li, key=lambda w: [sym.index(c) for c in w])


# 두번째 알고리즘 : 5.87 ms ± 649 µs per loop (mean ± std. dev. of 20 runs, 100 loops each)
def print_ordered_sym2(sym,n,out_file):
    alphabet=' '+sym
    for x in product(alphabet,repeat=n):
        xs = ''.join(x).strip()
        if not x[0] == ' ' and not ' ' in xs:
            print(xs,file=out_file)

with open('rosalind_lexv.txt') as file:
    # make input
    sym = file.readline().rstrip().replace(' ','')
    n = int(file.readline().rstrip())

# with open('lexv_out.txt','w') as out_file:
#     # use function
#     for word in print_ordered_sym(sym,n):
#         print(word,file=out_file)

with open('lexv_out2.txt','w') as out_file:
    # use function2
    print_ordered_sym2(sym,n,out_file)

