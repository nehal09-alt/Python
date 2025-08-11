# wap a recursive function to calculate the sum of first n natural numbers.


def natural (n):
    if (n==1  ):
        return 1
    if (n==0):
        return 0 
    
    else :
        return n +(natural(n-1))
    

print (natural(0))    

istl= ["asad", "nehal ", "Jishan", " kallu briyani "]
def fukra (istl ):
     print (len (istl))
     return (istl)


print (fukra (istl ))

#2 second way to solve it :;

def print_list (list,idx=0):
    if (idx==len(list )):
        return 
    print (list [idx])
    print_list (list,idx+1 )




print (print_list(istl))