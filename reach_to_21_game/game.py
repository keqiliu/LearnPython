# the cute game
import random


def get_add_number(current_num):
    if current_num % 3 == 2:
        return 1
    elif current_num % 3 == 1:
        return 2
    else:
        return random.randint(1, 2)


if __name__ == '__main__':
    print('\n{game_name:-^40}'.format(game_name='let\'s play a game'))
    print('start with 1 or 2, then adNd 1 or 2 onto it')
    print('whoever reaches 21 wins!')
    print('\nAre you ready? :)\n')
    player_goes_first = str(input('Do you want to go first? Y/N?'))
    if player_goes_first.lower() == 'n':
        player_goes_first = False
        print('OK. ', end='')
    else:
        player_goes_first = True
        print('Cool. So you go first.')

    num = 0
    while 1:
        if not (num == 0 and not player_goes_first):
            player_num = int(input('\nAdd 1 or 2 ?'))
            if player_num not in [1, 2]:
                print('Must be 1 or 2')
                continue
            num += player_num
            print('OK. You reach', num)
            if num >= 21:
                print('Hooray! You win! ^_^'.format(num))
                break

        my_num = get_add_number(num)
        num += my_num
        print('My turn: I\'m gonna add {0},\t'.format(my_num), end='')
        print('so now we get', num)
        if num >= 21:
            print('Ah-ha! I got you. :)'.format(num))
            break
