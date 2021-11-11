
array2 = []
def create_array (width:int, height:int):
    for _  in range (height):
        array2.append(list(' ' * width))


create_array (3,3)
print (array2)