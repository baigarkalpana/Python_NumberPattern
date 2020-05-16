"""
Author:Kalpana Baigar

Program to print following Number pattern

1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9

"""

size=int(input("enter number"))

def display(num):
    cnt=0 
    for i in range(1,num+1):
        cnt=i
        for j in range(1,num+1):
            print(cnt,end=" ")
            cnt+=1
        print()      
        


display(size)

