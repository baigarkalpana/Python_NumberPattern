'''
Author:Kalpana Baigar

Program to print following number pattern

1  2  3  4
5  6  7  8
9  10 11 12
13 14 15 16

'''

def display():
    size=int(input("enter number"))
    cnt=1
    for i in range(1,size+1):
        for j in range(1,size+1):
            print(cnt,end="\t")
            cnt+=1
        print()



display()
