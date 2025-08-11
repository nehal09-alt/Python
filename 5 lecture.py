# loops 
#REPEAT INSTRUCTION 
 
# WHIILE LOOPS 


count = 1
while count <=5:
    print ("hello world ")
    count +=1


# practise question on while loops 


#print number from 1 to 100.


i = 1 
while i <=100 :
    print (i )
    i +=1 

# print 100 t0 1


i =100 
while i >=1:
    print (i)
    i -=1



# print the multiplication table of a number n .

print ("table ")
n = int (input ( "enter your table number : " ))
i = 1
while  i <=10:
    print (n*i)
    i +=1

print ('question of while ')

# print the elemnts of the following list in loops :

#{1,4,9,16,25,36,49,64,81,100}

print (" uses  of while loops ")
num = [ 1,4,9,16,25,36,49,64,81,100]
i= 0
while i < len(num):
    print (num [i])
    i+=1


# search the x in following tuples 
print (" uses of while loops ")
num = (1,4,9,16,25,36,49,64,81,100)
x = int (input ( "found your number = "))
 
i = 0
while i < len(num ):
    if (num [ i ]  ==x) :
        print ("found  it :", i)
    else :
        print ("not found ")
    i +=1 
 
# BREAK & CONTINUE 

# break 
print ("break")
i =1
while i<=5 :
    print (i)
    if (i==3 ):
        break 
    i+=1
# continue 
print ("continue ")
i = 1 
while i<=5 :
    if (i ==3 ):
        i+=1
        continue # skip 
    print (i)
    i+=1

#! while loop for even number 

i=1 
while i<=10:
    if(i%2 != 0 ) :
        i+=1 
        continue
    print (i)
    i+=1

print ("for loops" )

# for loops 

nums = [ 1,2,3,4,5,6]
for val in nums : # use for loops 
    print (val)
else:
    print ("END  of loop")

# qustion ussing for loop

#print the element of the  following 
#{1,4,9,16,25,36,49,64,81,100}

list = {1,4,9,16,25,36,49,64,81,100}
for nums in list:
    print (nums )
else :
    print ("end ")


# search for a number x in tuple using loop :
# [1,4,9,16,25,36,49,64,81,100]

tuple = (1,4,9,16,25,36,49,64,81,100)

x = int (input ("search = "))
idx = 0
for num in tuple :
    if (num ==x):

        print ("found ", idx )
    idx +=1

# range() function :

for i in range (10):
    print (i)



# range (start , stop , step ):


for i in range (10 , 100, 10):
    print (i)

# pass statement :
#jab loop ma kuch nahi karna hai


for i in range (1,5 ):
    pass 
