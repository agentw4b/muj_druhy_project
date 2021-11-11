playing_stones: list = ["X", "O"]
initial_char = ' '


def create_array(width:int, height:int):
    array = []
    for _  in range (height):
        array.append(list(initial_char * width))
    return array

def print_array(array:list):
    print(len(array))
    for line in range(0,len(array)):
        print(f'{array[line]}\n')

#main program
array1 =[]
array1 = create_array (3,3)
print_array(array1)