# wap to ask the user to enter names of their 3 favourite movies &store them in a list.

movies=[]
firstmovies = input ("Enter the 1 movies name ")
secondmovies =input("Enter the second movies name ")
thirdmovies = input ("Enter the third movies name ")

movies.append(firstmovies)
movies.append(secondmovies)
movies.append(thirdmovies)
print (movies)
print (type (movies))

# wap to check if a list contains a palindrome of element .
 

list =  [1,2,1]

copy=list.copy()
copy.reverse()

if (copy==list):
    print ("palindrome ")
else :
    print ("Not palindrome ")


    # wap to count the number of student with the grade "a "grade in the following :
   # ["c","d","a","a","b","b","a"]

tup= ("C","D","A","A","B","B","A")

print (tup.count ("A")) 
print (tup.count ("B"))
print (tup.count ("C"))
print (tup.count ("D"))


list =["C","D","A","A","B","B","A"]
list.sort()
print (list)
