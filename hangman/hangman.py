from words import words
import random
import string
def get_valid_word(data):
    word = random.choice(data)
    while '-' in word or ' ' in word:
        word = random.choice(data)
    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(word_letters) != 0 and lives > 0:
        print('='*30)
        print('used_letters: ',' '.join(used_letters))
        word_pretty = [letter if letter in used_letters else '-' for letter in word]
        print(' '.join(word_pretty))
        letter = input('Enter the letter: ').upper()
        if letter in used_letters:
            print('You have used these letter. Try again')
        elif letter in alphabet - used_letters:
            used_letters.add(letter)
            if letter in word_letters:
                word_letters.remove(letter)
            else:
                lives -= 1
                print('You have |',lives, '| lives')
        else:
            print('Something get wrong. Enter a correct letter')

    print('=*' * 10 + 'END OF THE GAME' + '=*' * 10)
    if lives == 0:
        print("You DIED")
    else:
        print("CONGRATULATIONS. You win!")


hangman()


