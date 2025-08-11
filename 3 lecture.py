# 3 list and tuples

 
str = ["Nehal" ," Jishan ", "Sana" ]
print (str)
print (type (str))
print (str[2])

 #strings = immutable ( change nahi hoga )
#list = mutable ( change hoga )

#example 

student = [ "Nehal","jishan" ,"Sana" ," shahzadi" ]

student [0]= "henery"
print (student )


# list slicing 

marks = [ 34,56,78,98,23]
print(marks[1:4])
print (marks [:5])
print (marks [1:])
print (marks [-4:-3])

#list methods

list = [ 12,23,6,4]
list.append (78)  # append ka matlab last ma khuch bhi add kar lata hai
print (list )

list .sort () # sort matlab assending ordder 
print (list)


list.sort(reverse =True ) # dessending order 
print (list )

list.reverse() # purab list ka ulta kar daga 
print (list)


list  .insert(2,7) # number add kar daga 
print (list)

list .remove (7) # number ko remove kar daga 
print (list )


list.pop(2)
print (list )
 # or bhi bhot methods hai padhlo ""


 # tuples 


tup=(23,34,45,67,78)
print (tup)
print (type(tup))

# smae as list but ya IMMUTABLE HAI
# tuple methods 
tup=(2,4,6,8,10)

print (tup.index(10))

print (tup.count (2))




