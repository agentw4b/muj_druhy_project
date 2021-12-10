playing_stones: list = ["X", "O"]
initial_char = '_'


def create_array(size):
    array = []
    for _  in range (size):
        array.append(list(initial_char * size))
    return array

def print_array(array:list):
    print(len(array))
    for line in range(len(array)):
        print(f'{array[line]}\n')

#main program
array1 =[]
array1 = create_array (5)
print_array(array1)

