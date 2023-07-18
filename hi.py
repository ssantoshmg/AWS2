for i in range(1,21):
    if i %2 ==0:
        print(i)

#Function is block of code that perfrom specific task
#function is only run when it's call
#by usin def keyword we can defindd the function
#example def function naamed


def add():
    print("SANTOSDH ")
add()


def ad(a,b):
    c = a+b
    print("ADDITION =" ,c)
ad(2,3)
ad(4,5)
ad(4.5, 4.5)
ad(7,7)

def mul(a,b,c):
    d =a*b*c
    print("MULTPLUICATION IS",d)
mul(5,6,9)
mul(5,6,10)
mul(5,6,34)


def hi(fname):
    print(fname,"GAIKWAD")
hi('SANTOSH')
hi('PIU')
hi('ANJU')
hi('APP')
hi('KUSUM')

def hello(fname ,lname):
    print(fname ,lname)
hello('SANTOSH','GAIKWAD')
hello('SANTOSH','mali')


def anju(*hi):
    print("THIS IS HOW QE ",hi[2])
anju('SANTOSH','HAHAHAH',23)







