#1   store following word meaning in pyhton dictionary :
# table :"a piece of furnitrue ", "list of facts &figures "
#cat :"a small animal"


dictionary = {
    "cat ": "a small animal ",
    "table": [ " a piece of funitrue ", "list of figures "]
}
print (dictionary)
print (type (dictionary ))

# you are given a list of subjev=cts for student . assume one classroom is required for 1 subjects .
# how many classroom are needed by all student .
#"python ", java , c++, javascript , java , python java ,c++ , c.



subject =  {
    "python ", "java ", "javascript", "c++","c" ,"java ","python ","java ","python ", "c++"
}
print (len (subject))



#3 wap to enter marks of 3 subjects from the user and store them in dictionary .
# start with an empty dictionary &add one by one . use subject name as key & mark the value .


marks = {}
a = int (input (" enter phy : "))
marks.update({"phy":a })
b = int (input (" enter chem : "))
marks.update({"chem":b})
c = int (input (" enter math: "))
marks.update({"math":c})

print (marks)

#figure out a way to store 9 &9.0 

values ={
    9, "9.0"
}
print (values )
  #2 
values = {
    ("int ", 9),
    ("float ", 9.0)

  }
print (values )