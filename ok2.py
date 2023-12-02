import time
a=int(input("введите часы"))
b=int(input("введите минуты"))
c=int(input("введите секунды"))
while True:
    if b >= 60:
        a+=1
        b=0
    if c >= 60:
        b+=1
        c=0
    if a >= 24:
        a=0
    c+=1
    print(a,":",b,":",c)
    time.sleep(1)