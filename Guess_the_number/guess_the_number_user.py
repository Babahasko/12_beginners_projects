import random


def guess_pc(x):
    high = x
    low = 1
    feedback = ''
    while feedback != 'c':
        if low == high:
            sample = low
        else:
            sample = random.randint(low, high)
        feedback = input(f'Is {sample} lower(l), higher(h) or it is correct(c)?: ')
        if feedback == 'l':
            low = sample + 1
        if feedback == 'h':
            high = sample - 1
    print('''\
    Congratulations!!! I guessed your number!)))
    ''')


if __name__ == '__main__':
    print("=" * 10 + "GUESSING GAME FOR PC" + "=" * 10)
    print('''\
    Hi! It is guessing number game, where you guess
     the number and your pc try to guess it.
    ''')
    guess_pc(1000)
