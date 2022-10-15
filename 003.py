a, b, c = map(int, input().split())
list1 = [a, b, c]
if (a==b) and (b==c) :
    print(10000+1000*a)
elif (a==b) :
    print(1000+100*a)
elif (b==c):
    print(1000+100*b)
elif (a==c):
    print(1000+100*c)
else :
    print(max(list1)*100)