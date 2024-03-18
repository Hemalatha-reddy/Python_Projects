import random
position={'top-l':' ','top-m':' ','top-r':' ','mid-l':' ','mid-m':' ','mid-r':' ','bot-l':' ','bot-m':' ','bot-r':' '}
def display_board():
    print("{} | {} | {}".format(position['top-l'],position['top-m'],position['top-r']))
    print("- + - + -")
    print("{} | {} | {}".format(position['mid-l'],position['mid-m'],position['mid-r']))
    print("- + - + -")
    print("{} | {} | {}".format(position['bot-l'],position['bot-m'],position['bot-r']))
display_board()
def game():
    for chances in range(0,3):
        move=input('turn for x player,enter your position:')
        if position[move]==" ":
            position[move]='x'
        else:
            print('wrong position')
            move=input('enter your position X player:')
            if position[move]==" ":
                position[move]='x'
        display_board()

        print('computer turn')
        move=random.choice(list(position.keys()))
        if position[move]==" ":
            position[move]='0'
        else:
            print('wrong position')
            move=random.choice(list(position.keys()))
            if position[move]==" ":
                position[move]='0'
        display_board()
        if (position['top-l']=='x' and position['top-m']=='x' and position['top-r']=='x') or (position['mid-l']=='x' and position['mid-m']=='x' and position['mid-r']=='x') or (position['bot-l']=='x' and position['bot-m']=='x' and position['bot-r']=='x') or (position['top-l']=='x' and position['mid-m']=='x' and position['bot-r']=='x') or (position['top-r']=='x' and position['mid-m']=='x' and position['bot-l']=='x') or (position['top-l']=='x' and position['mid-l']=='x' and position['bot-l']=='x') or (position['top-m']=='x' and position['mid-m']=='x' and position['bot-m']=='x') or (position['top-r']=='x' and position['mid-r']=='x' and position['bot-r']=='x'):
            print('player X is winner')
        if (position['top-l']=='0' and position['top-m']=='0' and position['top-r']=='0') or (position['mid-l']=='0' and position['mid-m']=='0' and position['mid-r']=='0') or (position['bot-l']=='0' and position['bot-m']=='0' and position['bot-r']=='0') or (position['top-l']=='0' and position['mid-m']=='0' and position['bot-l']=='0') or(position['top-r']=='0' and position['mid-m']=='0' and position['bot-l']=='0') or (position['top-l']=='0' and position['mid-l']=='0' and position['bot-l']=='0') or (position['top-m']=='0' and position['mid-m']=='0' and position['bot-m']=='0') or (position['top-r']=='0' and position['mid-r']=='0' and position['bot-r']=='0'):
            print('player 0 is winner')
game()
def win_logic():
    if (position['top-l']=='x' and position['top-m']=='x' and position['top-r']=='x') or (position['mid-l']=='x' and position['mid-m']=='x' and position['mid-r']=='x') or (position['bot-l']=='x' and position['bot-m']=='x' and position['bot-r']=='x') or (position['top-l']=='x' and position['mid-m']=='x' and position['bot-r']=='x') or (position['top-r']=='x' and position['mid-m']=='x' and position['bot-l']=='x') or (position['top-l']=='x' and position['mid-l']=='x' and position['bot-l']=='x') or (position['top-m']=='x' and position['mid-m']=='x' and position['bot-m']=='x') or (position['top-r']=='x' and position['mid-r']=='x' and position['bot-r']=='x'):
        print('player X is winner')
    elif (position['top-l']=='0' and position['top-m']=='0' and position['top-r']=='0') or (position['mid-l']=='0' and position['mid-m']=='0' and position['mid-r']=='0') or (position['bot-l']=='0' and position['bot-m']=='0' and position['bot-r']=='0') or (position['top-l']=='0' and position['mid-m']=='0' and position['bot-l']=='0') or(position['top-r']=='0' and position['mid-m']=='0' and position['bot-l']=='0') or (position['top-l']=='0' and position['mid-l']=='0' and position['bot-l']=='0') or (position['top-m']=='0' and position['mid-m']=='0' and position['bot-m']=='0') or (position['top-r']=='0' and position['mid-r']=='0' and position['bot-r']=='0'):
        print('player 0 is winner')
    else:
        print('it is a draw match blw X and 0')
win_logic()
