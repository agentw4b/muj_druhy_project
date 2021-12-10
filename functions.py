def create_array(size, initial_char):
    array = []
    for _  in range (size):
        array.append(list(initial_char * size))
    return array

def print_array(array:list):

    for line in range(len(array)):
        print(f'{array[line]}\n')

def print_introduction():
        print('Welcome to Tic Tac Toe')
def print_rules():
        print('GAME RULES:Each player can place one mark (or stone)per turn on the 3x3 grid. The WINNER iswho succeeds in placing three of theirmarks in a:* horizontal,* vertical or* diagonal row========================================Lets start the game')
