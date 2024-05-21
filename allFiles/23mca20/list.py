#lis=(input("enter the list of integer"))
def remove_dublicate(list_num):
    super_list=[]
    for num  in list_num:
        if num not in super_list:
            super_list.append(num)
    return super_list
def discard_list(super_list):
    new_list=[]
    for num in super_list:
        if num%3==0:
            if num >30:
                new_list.append(num+5)
            else:
                new_list.append(num- 5)
    return new_list
            

lis=input("enter a list of integer with *space*:").split()
list_num=list(map(int,lis))
super_list = remove_dublicate(list_num)
print("the super list is :",super_list)
next_list=discard_list(super_list)
print("the new list:",next_list)

