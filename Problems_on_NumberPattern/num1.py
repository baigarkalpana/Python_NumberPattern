'''
Author:Kalpana Baigar
Program to printing following number pattern

    11111
    11111
    11111
    11111
    11111

'''

def display(no):

    for i in range(1,no+1):
        for j in range(1,no+1):
            print("1",end=" ")
        print()




num=int(input("enter number"))

display(num)
