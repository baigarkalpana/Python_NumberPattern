"""
Author:Kalpana Baigar
Progarm to print following Number pattern 
1
2 2
3 3 3
4 4 4 4
"""


def display(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
             print(i,end=" ")
        print()     


size=int(input("enter number"))
display(size)
