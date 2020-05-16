'''
Author:Kalpana Baigar

Program to print following number pattern

1111
2222
3333
4444
5555

'''

size=int(input("enter size"))

for i in range(1,size+1):
    for j in range (1,size+1):
        print(i,end=" ")
    print()
