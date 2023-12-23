# a = 0
# b = input()
# for k in b.split():
#    if a % 2 == 0:
#       print(k)
#    a += 1
list=input().split()
h=int(input())
a=0
for k in range (len(list)):
    if int(list[k]) >= h:
        a+=1
print(a+1)