import random
import string
available_letters = list(string.ascii_uppercase)


def play_game():
    with open('words.txt') as my_file:
        read_file = my_file.read()
    word_list = read_file.split()
    low_mystery_word = (random.choice(word_list))
    mystery_word = low_mystery_word.upper()
    word_length = len(mystery_word)
    unpacked = [*mystery_word]
    blank_list = unpacked[:]

    i = 0

    while i < len(blank_list):
        blank_list[i] = '_'
        i += 1

    print(*blank_list)

    print(mystery_word)

    print(unpacked)

    print(f'The mystery word is {word_length} letters long.')
    print('')
    guess_count = 0
    guessed_list = []
    while guess_count < 8 and '_' in blank_list:
        print('')
        print(f'Guesses remaining: {8 - guess_count}')
        print('')
        print('Available letters to guess:')
        print(available_letters)
        print('')
        guess = input('Guess a letter: ').upper()
        if not guess.isalpha() or len(guess) != 1:
            print('')
            print('Invalid guess. Please guess one letter.')
            continue
        elif guess in guessed_list:
            print('')
            print('You have already guessed this letter.')
            continue
        elif guess in mystery_word:
            available_letters.remove(guess)
            guessed_list.append(guess)
            
            print('')
            print('Good guess!')
            print('')

            continue
        else:
            guess_count += 1
            available_letters.remove(guess)
            guessed_list.append(guess)
            print('')
            print('Incorrect guess')
            continue

    if '_' in blank_list:
        print('')
        print('Sorry! You lose!')
    else:
        print('')
        print('Congratulations! You win!')


if __name__ == "__main__":
    play_game()
