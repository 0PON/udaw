n=input("введите число ")

a=24
f=n//60
n%=60
if f/a>=1:
    f%=24

print(f,":",n)