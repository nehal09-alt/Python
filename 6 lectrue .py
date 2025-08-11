# function 
# average of 3 number

def calc_avg (a,b,c):
    sum = a+b+c
    avg =sum/3 
    print (avg)
     


calc_avg (2,4,6)



#waf  to print the length of a llist . (list is the perameter )


def nehal_name ():
    print ("mango , grapes , aplle , alpha ,apllo" , end = " &") 
    print (len("mango , grapes , aplle , alpha ,apllo"))
# end = ka matlb space nahi hoga 
nehal_name ()
 




nehal_name ()



#
vegies = ["mango ", "grapes" , "aplle" , "alpha" ," apllo"]
def fruits_name (list ):
    print (list)
    print (len(list))
    



fruits_name (vegies )

# WAP to find the factorial on n. : (n is the parameter ):


#n = 3
#facto=1
#for i in range (1,n+1):
    #facto*=i

#print (facto )


def facto(n):
    facto=1
    for i in range (1,n+1):
       facto*=i
    print (facto )


facto (5)

facto (120)


# usd to inr 

def usd_inr (n ):
    usd = 83 
    inr =n *usd 
    print (n ,"$ usd =", inr , "INR" )


usd_inr (3)


#2 odd & even 

def odd_even (a):
       if a % 2 == 0:
      
        print (a , "is even")
       else :
        print (a, "is odd ")


odd_even(101)


# RECURSION 
# is like A loop but its a function  call itself 
# we can use both , they work as same .

def show(n):
    if (n==0):
        return
    print (n )
    show(n-1)
    print ("END")

show (6) 


def facto (a):
    if (a ==1 or a==0):
        return 1 
    else :
        return facto(a-1)*a


print (facto (3))