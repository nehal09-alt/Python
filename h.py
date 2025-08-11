# list = [1,7,8,9,5,-4,-9,5,-9,-2]
# i = 0 
# for num  in list :
#     if num> 0 :
#         i+=1
# print(i)

# n =  int(input("enter : "))
# i = 0 
# while i <= n :
#     if(i%2==0):
#         print(i)
#     i+=1

# k = int(input("enter : "))

# i = 1
# while i<=10:
#     print(i*k)
#     i+=1

# str = (input("enter : "))
# reversed_str = ""
# for char in str :
#     reversed_str = char + reversed_str
# print(reversed_str)

# pip = "tetter"

# for char in pip:
#     print(char)
#     if pip.count(char)==1:
#         print("char is :",char)
#         break



# while True:
#     ask = int(input("enter : "))
#     if 1<= ask <= 10: 
#         print("ok")
#         break
#     else:
#         print("try again")

# print("hogaya mat kar maya ko hasan kya kal sai manjhi ")

# name = input("Enter your Name: ")
# Age = input("Enter your Age : ")
# blood_suagr =int(input("Enter your Blood counting : "))
# group = input("enter your blood group ")
# if blood_suagr> 62 :
#     print("Patients",name ,"/n",Age,"/n", "Blood-Group", group)
#     print("patitents has Diabetes ")
# else:
#      print("Patients",name ,"/n","Age : ", Age,"/n", "Blood-Group", group)
#      print("Patients has No Diabetes ")



def main (x , y ):
    print("sum of x =",x ," y = ",y," is : ",x+y)


main(2,4)


def multiply(x , y ):
    print(x*y)

multiply("vvvv",2)

def radius( p , r):
    area = p*(r**2)
    circumference = 2 *(p*r)
    print("area is ",area )
    print("circumferene is ",circumference )

radius(3.14 , 3)

def sum(*args):
    return sum(args)

sum((1,2,3,4,5,6))