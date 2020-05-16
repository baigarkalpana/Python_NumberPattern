"""
Author:Kalpana Baigar
Progarm to print following Number pattern 

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1


"""


def display(num):
    for i in range(1,num+1):
        cnt=i
        for j in range(1,i+1):
          print(cnt,end=" ")
          cnt-=1

        print()     


size=int(input("enter number"))
display(size)
