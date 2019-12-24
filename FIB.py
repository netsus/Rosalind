def rabbit(n,k):
    small=1
    big=0
    for i in range(n-1):
        small,big = big*k,big+small
    return(small+big)
