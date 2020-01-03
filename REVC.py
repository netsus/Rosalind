"""
난이도 : 1

문제 : 주어진 서열에 대해 reverse 상보서열을 출력

알고리즘 : str.maketrans로 한 문자에서 다른 문자로 조회 가능한 테이블을 생성한다.
    주어진 서열을 seq에 저장하고 seq[::-1]로 뒤집고, seq[::-1].translate() 함수에 위에서 생성한 테이블을 인자로 넣어
    최종적으로, reverse 상보서열을 반환한다.
    rna일때 따로 지정가능
"""
complement_DNA_table = str.maketrans("ATGC","TACG")
complement_RNA_table = str.maketrans("AUGC","UACG")

def reverse_complement(seq, rna=False):
    if rna:
        return seq[::-1].translate(complement_RNA_table)
    else:
        return seq[::-1].translate(complement_DNA_table)

with open('rosalind_revc.txt') as file:
    seq = file.readline().rstrip()
    print(reverse_complement(seq))
