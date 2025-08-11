# second day of pyython 
########## .day 2 ##### ( 06/09/2024)


print (" nehal is a good boy \n bkl")
print (" nehal is a good boy \t bkl")
print (len(" nehal is a good boy \n bkl"))

computer = "laptop"
ch = computer [5]
print (ch)
print (computer[0:4])
print (computer[-3:-2])


#string function # 
# 1 endswith ()
#2  capitalize ()
#3 replace ()
#4 find ()
#5 count()

str = " i am learning python from apna app"
print (str. endswith ("app"))
print (str.capitalize ("i"))
print (str. replace ("o" , "a"))
print (str. find ("o"))
print (str. count ("a"))



########### 

## conditional statement #####



# if 
#elif 
#else 



#1 "if "

#age = 18 
#if (age >=18 ):

   # print ("can drink")


#2 "elif "

light = "green "
#if (light ==  "yellow "):
 #   print ("slow")
#elif (light == "green " ):
  #  print ("go ")
#elif (light =="red" ):
   # print (" stop ")


###3 else 


light = "black"
if (light ==  "yellow "):
    print ("slow")
elif (light == "green " ):
    print ("go ")
elif (light =="red" ):
    print (" stop ")
else:
    print ("teri maa ki chut ")




# example of every thing (if , else , elif )


#marks = int (input (" enter the marks: "))

#if (marks >= 90 ):
    #grade = "A"
    
#elif (marks >=80 and marks <90):
    #grade ="B"
#elif ( marks >=70 and marks < 80 ):
    #grade = "C"
#else:
    #print (" grade d")




    # double if use capable 



    
age = 23
if (age >= 18):
    if (age >= 80):
        print (" you can not drive ")
    else:
        print ("you can drive ")

else:
    print (" you cannot drive ")
    