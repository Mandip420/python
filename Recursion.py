def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n* factorial(n-1)
d=factorial(5)
print(d)
print(factorial(4))