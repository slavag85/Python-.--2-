
import random  
   
my_list = [random.randint(0,100) for _ in range(10)]  
 
 print (my_list)

for i in range(len(my_list)):
    k = random.randint(0,(len(my_list)-1))
    my_list[i], my_list[k] = my_list[k], my_list[i]

print(my_list)