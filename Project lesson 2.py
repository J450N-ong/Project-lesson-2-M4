def prod(val) : 
    res = 1
    for ele in val: 
        res *= ele 
    return res  
  
tup1 = (4, 3, 2, 2, -1, 18) 
  
print("The original tuple is : " + str(tup1)) 
 
res = prod(list(tup1)) 
  
print("The product of tuple elements are : " + str(res)) 

tup2 = (2, 4, 8, 8, 3, 2, 9) 
  
print("The original tuple is : " + str(tup2)) 
 
res = prod(list(tup2)) 
  
print("The product of tuple elements are : " + str(res)) 