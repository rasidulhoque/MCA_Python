#def display_tuple(tup_elm):
  #  print(tup_elm)

def sumation_tuple(tup_elm):
    total = 0
    for element in tup_elm:
        total = total + element
    return total

def count_occurence(tup_elm):
    count= 0
    for element in tup_elm:
            count +=1
        else:
            count=1 
    return count
            
tup = input("enter the element of tuple: ").split()
tup_elm = tuple(map(int, tup))
print("the sum of the elements is", sumation_tuple(tup_elm))
print("the count of the element is ", count_occurence(tup_elm))
