def convert_num_list_to_num(str_num_list): 
    numlist=[]
    for item in str_num_list:   
        num=int(item)
        numlist.append(num)  
    return numlist


str_num_list= input().split(",")
rotate_times=int(input())
num_list=convert_num_list_to_num(str_num_list)

len_list=len(num_list)
slicing_index = rotate_times % len_list 

first_part= num_list[ :slicing_index]  
second_part=num_list[slicing_index:]
#print(first_part)
#print(second_part)
second_part.extend(first_part)
print(second_part)