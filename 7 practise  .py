# create a new file "practce .txt "using python add data follwing onit :


with open(" prctice .txt","w") as f :
    f.write(" hi Everone \n we are learning file I/O \n using java . \n I like programing in java and python")


with open (" prctice .txt","r")as f :
    data = f.read()
    
new_data = data.replace ("java","Python")
print(new_data)
 
with open (" prctice .txt","w")as f :
    data = f.write (new_data)

with open (" prctice .txt","r")as f :
    data = f.read()
    if (data .find ("leraning ")):
        print ("found ")
    else:
       print ("not found ")


def check_foline ():
    with open (" prctice .txt","r")as f :
        data = f.read()

        if (data .find ("leraning ")):
           print ("found ")
        else:
          
          print ("not found ")



check_foline()


def check_inline ():
     word ="python"
     data = True 
     line_no =1 
     with open (" prctice .txt","r")as f :  
        while data:
            data= f.readline()
            if (word in data ):
                return
            line_no +=1
         
        

check_inline()

#from file contaning number separated by comma ,print the count of even number :


with open (" prctice .txt","r")as f :
    data = f.read()
    print (data )