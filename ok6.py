# №1) s=input()
# if s.find("борщ") !=-1:
#    print("да")
# else:
#    print("нет")
# print(input().count(' ')+1)

a=input()
c=a[0:a.find(" ")]
d=a[a.find(" ")+1:len(a)]
print(d,c)