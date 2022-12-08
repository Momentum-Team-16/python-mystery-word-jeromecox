import random
import string
available_letters = list(string.ascii_uppercase)


def play_game():
    with open('words.txt') as my_file:
        read_file = my_file.read()
    word_list = read_file.split()
    low_mystery_word = (random.choice(word_list))
    mystery_word = low_mystery_word.upper()
    print(mystery_word)

    print(f'The mystery word is {len(mystery_word)} letters long.')

    guess_count = 0
    guessed_list = []
    while guess_count < 8:
        print('Available letters to guess:')
        print(available_letters)
        guess = input('Guess a letter: ').upper()
        if not guess.isalpha() or len(guess) != 1:
            print('Invalid guess. Please guess one letter.')
            continue
        elif guess in guessed_list:
            print('You have already guessed this letter.')
            continue
        elif guess in mystery_word:
            guess_count += 1
            available_letters.remove(guess)
            print('Good guess!')
            print(f'Guesses remaining: {8 - guess_count}')
            continue
        else:
            guess_count += 1
            available_letters.remove(guess)
            print('Incorrect guess')
            print(f'Guesses remaining: {8 - guess_count}')
            continue


if __name__ == "__main__":
    play_game()
