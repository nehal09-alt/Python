# dictionary & sets

# dictionary are mutable 
"""Key : value """
info = {
    "name": " Nehal",
    "list": [ "nehal ", " Jishan ", "Sana"],
    "tuples ": ("teri ", "Meri",),
    "int ": 34,
    "float ": 32.56,
    }
print (info )
print (type(info))


print (info["name"])
info["name"]= "papa ka naam puch raha hai"
print (info)

# null dict 

null_dict={}
null_dict["kaam "]= "nahi malum"
print (null_dict)


# nested dictionary

carrer= {
    "name ": "Nehal",
    "subj": {
        "phy": 45,
        "comput":98,
        "geog": 56,
    } 
    }
print (carrer)
print (carrer ["subj"])
print (carrer ["subj"]["comput"])

# dictionary methods

print (carrer.keys())
print(carrer.values())
print (carrer.items())
print (carrer.get("subj"))
carrer .update ({ "city": "kolkata",})
print (carrer)

# sets 
# Each item in the set are immutable and unique 


collection ={1,2,4,"nehal", "jishan",1,4,2}
print (collection )
print (type(collection ))

print (len(collection))

# empty set 
hello = set()
print (hello)
print (type(hello))


#set.add(el)
#set.remove(el)
#set.clear()
#set.pop() # remove random value 
#set.union(set2)
#set.intersection(set2)


hello = set()
hello.add(1)
print(hello)


set1 ={ 1,3,5,7,9,11,4,6,10}
set2 ={0,2,4,6,8,10,1,9}
print (set1.union(set2))
print (set1.intersection(set2))


 ### end 24 /09/24###