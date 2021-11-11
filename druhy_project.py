

def create_array (width:int, height:int):
    array = []
    for _  in range (height):
        array.append(list(' ' * width))
    return array

array1 =[]
array1 = create_array (3,3)
print (array1)