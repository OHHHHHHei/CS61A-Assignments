def is_prime(n):
    if  n < 2:
        return False
    i = 2
    isprime = 1
    while i < n:
        if n % i == 0:
            isprime = 0
            break   # �ҵ����Ӻ������˳�
        i += 1
    if isprime == 0:
        return False
    else:
        return  True
            
