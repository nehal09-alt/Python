# file function 
# input or output 

# how to make file and read 

f = open ("demo.txt", "w")
data = f.write (" i am Nehal \n i making this file ")
print (data )
f.close

# open and read file 

f =open ("demo.txt","r")
data = f.read()
print(data)
print (type(data))
f.close 

# there are many function to read and write 
# (r, w, a , x , b , t , +)
# a = append , X = create a new file   , b = binary t = text mode ,+ = open adisk file for updating  
#agar koi file exists nahi karti to usko (w ya a) mode kholna hia 

f = open ("demo.txt", "a")
f.write  ( "\n mera naam nehal hai \n tumhar a naam kya hai ")
f.close 


f = open ("demo.txt ", "r")
data = f.read ()
print (data)
f.close  

# or detail ma 
# ( r+ , w+ , a+)
# r+ = read wnd write both isma over write ho jata hai 
# w+ =    read and write both isma over write ho jata hai but isma file phale jo tha wo delete hojata hai

# with syntax 

with open("nehal.txt","r") as f :
    data =f.read()
    print (data)

with open ("demo.txt","w") as f:
    f.write("new data ")

# import os  
# kuch bhi install karn aka liya 
# import name of module 
#install write pip and name of module 


