"""���� : 1���� �䳢�� �¾�� 2���� �Ŀ� k ���� �䳢�� ���´�. ó���� �� �¾ 1���� �䳢�� �����Ѵ�.
n���� �Ŀ� �䳢�� �ּ��� ��ȯ�Ͽ���.
�˰����� : �Ʊ��䳢 �ּ��� small, ū�䳢 �ּ��� big.
    1���� �Ŀ� ū�䳢 �ּ��� small+big, 1���� ���� �Ʊ��䳢 �ּ��� big * k �� (big���� �䳢�� k�־� �����ϱ�)
    �ݺ��Ͽ� ����"""

def rabbit(n,k):
    small=1
    big=0
    for i in range(n-1):
        small,big = big*k,big+small
    return(small+big)
