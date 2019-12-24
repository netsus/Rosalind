"""문제 : 1쌍의 토끼가 태어난지 2개월 후에 k 쌍의 토끼를 낳는다. 처음엔 막 태어난 1쌍의 토끼가 존재한다.
n개월 후에 토끼의 쌍수를 반환하여라.
알고리즘 : 아기토끼 쌍수가 small, 큰토끼 쌍수가 big.
    1개월 후에 큰토끼 쌍수는 small+big, 1개월 후의 아기토끼 쌍수는 big * k 쌍 (big쌍의 토끼가 k쌍씩 낳으니까)
    반복하여 리턴"""

def rabbit(n,k):
    small=1
    big=0
    for i in range(n-1):
        small,big = big*k,big+small
    return(small+big)
