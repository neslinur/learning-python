import random

def puzzle():
    words = ['tracker', 'ribbon', 'corkscrew', 'sawhorse', 'tranquility', 'hyacinth']
    password = random.choice(words)

    print('You enter a room with words scribbled on the walls:')

    for word in words:
        if word == password:
            print(word.capitalize())
        else:
            print(word)

    print('In front of you, you see a computer terminal asking you for a password.')
    guess = input('Password: ')
    while guess != password:
        print('Incorrect password.')
        guess = input('Password: ')

    print('The computer begins to glow.')
    print('The wall in front of you sinks into the ground.')

# room = [
#     'xxxxx',
#     'x..ex',
#     'x...x',
#     'x...x',
#     'xxxxx',
# ]
room = [
    'xxxxxxxxxxxxxx',
    'x..........pex',
    'xxxxxxxxxxxxxx',
]

def announce_walls(current_row, current_col):
    if room[current_row - 1][current_col] == 'x':
        print('There is a wall up')
    if room[current_row + 1][current_col] == 'x':
        print('There is a wall down')
    if room[current_row][current_col - 1] == 'x':
        print('There is a wall left')
    if room[current_row][current_col + 1] == 'x':
        print('There is a wall right')

def move(current_row, current_col, direction):
    new_row = current_row
    new_col = current_col

    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1
    else:
        print(f'You can not move {direction}. Try up, down, left, or right')

    if room[new_row][new_col] == 'x': # Hit a wall!
        print('You can not move that way')
        return current_row, current_col
    elif room[new_row][new_col] == 'p': # Activate puzzle
        puzzle()
        return new_row, new_col

    return new_row, new_col
    
player_row = 2
player_col = 2

while room[player_row][player_col] != 'e':
  announce_walls
  direction = input('What direction would you like to move? ')
  
  player_row, player_col = move(player_row, player_col, direction)

print('You have escaped!')