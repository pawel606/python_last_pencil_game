import random


def showtable(pencils):
    for i in range(pencils):
        print('|', end='')
    print()


def turn(player, pencils):
    if player == 'John':
        print("John's turn:")
        pencils = move(pencils)
        return ['Jack', pencils]
    elif player == 'Jack':
        print("Jack's turn:")
        pencils = botmove(pencils)
        return ['John', pencils]


def move(pencils):
    err_msg = "Possible values: '1', '2' or '3'"
    while 1:
        try:
            move = int(input())
            if move == 1 or move == 2 or move == 3:
                if pencils - move >= 0:
                    return pencils - move
                else:
                    print('Too many pencils were taken')
            else:
                print(err_msg)
        except ValueError:
            print(err_msg)


def checklosingposition(pencils):
    start = 5
    while start <= pencils:
        if pencils == start:
            return True
        start += 4
    return False


def winningposition(pencils):
    if pencils >= 4 and pencils % 4 == 0:
        return 3
    start = 3
    while start <= pencils:
        if pencils == start:
            return 2
        start += 4
    start = 2
    while start <= pencils:
        if pencils == start:
            return 1
        start += 4


def botmove(pencils):
    if pencils == 1:
        move = 1
        print(move)
        return pencils - move
    elif checklosingposition(pencils):
        move = random.randint(1, 3)
        print(move)
        return pencils - move
    else:
        move = winningposition(pencils)
        print(move)
        return pencils - move


def pencilsamount():
    print('How many pencils would you like to use:')
    while 1:
        try:
            pencils = int(input())
            if pencils == 0:
                print('The number of pencils should be positive')
            elif pencils < 0:
                print('The number of pencils should be numeric')
            else:
                return pencils
        except ValueError:
            print('The number of pencils should be numeric')


def first():
    possibleplayers = ['John', 'Jack']
    print('Who will be the first ({p1}, {p2}):'.format(p1=possibleplayers[0], p2=possibleplayers[1]))
    while 1:
        firstplayer = input()
        if firstplayer in possibleplayers:
            return firstplayer
        print("Choose between '{p1}', '{p2}'".format(p1=possibleplayers[0], p2=possibleplayers[1]))


def game():  # user is 'John' bot is 'Jack'
    pencils = pencilsamount()
    player = first()
    i = 1
    while pencils > 0:
        showtable(pencils)
        tmp = turn(player, pencils)
        player = tmp[0]
        pencils = tmp[1]
    print("{p} won!".format(p=player))


if __name__ == '__main__':
    game()