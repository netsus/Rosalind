
# coding: utf-8

"""
난이도 : 5.5

문제 : 서열(seq)과 d(정수)가 주어진다.
    서열에 대해 d개 이하의 염기가 다른 모든 서열을 출력하시오
    
알고리즘 :  
    for문을 통해 주어진 서열의 첫글자에대해, ATGC를 순차적으로 돌며
        다르면, 해당 염기로 시작하고, seq의 나머지 서열에 대해 d-1을 재귀호출
        같으면, 해당 염기로 시작하고, seq의 나머지 서열에 대해 d를 재귀호출
"""

# seq에대해 d개 이하의 염기가 다른 모든 서열을 리스트로 반환
def list_under_d_mismatch(seq,d):
    if d == 0: # seq에 대해 d==0 이면, seq와 0개의 염기가 다른 즉, seq와 동일한 서열 반환
        return [seq]
    if len(seq) == 1 and d >= 1: # seq가 1개이고, d가 1이상 이면, seq에 대해 염기가 모두 다른것을 반환
        return [base for base in 'ATGC'] # d가 1이 아니고, 1 이상인 이유 : seq와 서열이 앞부분이 일치하고 뒤에 d보다 적게 다르면 오류
                                        # 즉, seq과 뒷부분만 다른경우는 모든 경우를 출력한다.
    res=[] # 결과 담을 리스트        # 뒤에 for문에서 ATGC 순서대로 다 다르게 하나씩 맞춰가기 때문에 중복은 자동으로 걸러진다.
    
    # extend를 사용하는 이유 : 컬렉션에 대해 항상 그 인자를 리스트의 원소로 추가하기 위함.
    # 모든 염기에 대해
    for base in 'ATGC': 
        if seq[0] != base: # base와 pattern의 첫문자가 다르면, 해당base로 시작, pattern의 나머지 부분에 대해 d-1로 함수 재호출
            res.extend( base + suffix for suffix in list_under_d_mismatch(seq[1:], d-1) )
            
        else: # base와 pattern의 첫문자가 같다면, 해당base로 시작, pattern의 나머지 부분에 대해 d로 함수 재호출
            res.extend( base + suffix for suffix in list_under_d_mismatch(seq[1:], d) )
    return res

with open('rosalind_ba1n.txt') as file:
    seq = file.readline().rstrip()
    d = int(file.readline().rstrip())
    result_li = list_under_d_mismatch(seq,d)
    print('\n'.join(result_li))
