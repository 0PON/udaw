
def s(a,n):
    if n==0:
        return 1
    else:
        return a * s(a,n-1)
print(s(int(input()), int(input())))
