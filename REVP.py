
# coding: utf-8

# In[14]:


"""
난이도 : 2.5

문제 : FASTA 포맷으로 ID와 1 kbp를 넘지않는 하나의 서열이 주어진다.
    모든 palindrom(회문서열)의 시작 인덱스와 회문서열의 길이를 출력하시오. (1 based)
    (단, 회문서열의 길이는 4,6,8,10,12 중에서만 출력하시오. 즉, 4이상 12이하의 회문서열. [회문서열은 항상 짝수이다.])

알고리즘 : reverse_complement 함수는 입력받은 서열에 대해, 역 상보서열을 반환
    print_palindrom 함수에 주어진 서열을 입력하면 회문서열의 시작인덱스와 길이를 차례대로 출력한다.
    
    print_palindrom 함수에 seq이 입력되면
    for 문을 돌며 마지막에서 4번째 염기 인덱스 까지 만 반복한다. ( 회문서열의 최소길이가 4이므로 마지막염기에서 4번째 염기까지만 검사)
        시작 인덱스를 start 변수에 저장
        회문 서열은 앞부분과 뒷부분으로 나눌 수 있다. 앞부분과 뒷부분의 길이는 2,3,4,5,6 일것이다. 그러므로
        for 문을 돌면 range(2,7)을 반복하며 각 수를 gap 변수에 저장
            회문 서열의 앞부분 서열은 pre_string에 저장
            회문 서열의 뒷부분 서열은 post_string에 저장
            앞부분 서열 과 뒷부분 서열의 역 상보 서열이 같다면 -> 회문 서열 이라면
                1 based로 인덱스를 출력하고, 회문서열의 길이(gap * 2)를 출력. (gap은 앞부분 서열의 길이이자, 뒷부분 서열의 길이)

"""

# REVC 문제 참조
complement_DNA_table = str.maketrans("ATGC","TACG")
complement_RNA_table = str.maketrans("AUGC","UACG")

def reverse_complement(seq, rna=False):
    if rna:
        return seq[::-1].translate(complement_RNA_table)
    else:
        return seq[::-1].translate(complement_DNA_table)

def print_palindrom(seq):
    for start in range(len(seq) - 3):
        for gap in range(2,7):
            pre_string = seq[start : start + gap]
            post_start = start + gap
            post_string = seq[post_start : post_start + gap]
            if pre_string == reverse_complement(post_string):
                print(start+1, gap*2)

with open('rosalind_revp.txt') as file:
    # make input
    ID = file.readline().rstrip().replace('>','')
    seq=''
    for line in file:
        seq += line.rstrip()
        
    # use function
    print_palindrom(seq)

