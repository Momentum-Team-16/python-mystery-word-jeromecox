import random
# import string
# available_letters = list(string.ascii_uppercase)


def play_game():
    with open('words.txt') as my_file:
        read_file = my_file.read()
    word_list = read_file.split()
    low_mystery_word = random.choice(word_list)
    mystery_word = low_mystery_word.upper()
    unpacked = [*mystery_word]

    blank_list = []
    for letter in mystery_word:
        blank_list.append('_')

    print(mystery_word)

    print('')
    guess_count = 0
    guessed_list = []
    while guess_count < 8 and '_' in blank_list:
        print('')
        print(*blank_list)
        print('')
        print(f'Guesses remaining: {8 - guess_count}')
        print('')
        unpack_guessed = [*guessed_list]
        if len(guessed_list) > 0:
            print(f'You have already guessed: {unpack_guessed}')
        # print('Available letters to guess:')
        # print(available_letters)
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
            # available_letters.remove(guess)
            guessed_list.append(guess)
            for i in range(len(blank_list)):
                # print(unpacked[i])
                if unpacked[i] in guessed_list:
                    blank_list[i] = unpacked[i]

            print('')
            print('Good guess!')
            print('')

            continue
        else:
            guess_count += 1
            # available_letters.remove(guess)
            guessed_list.append(guess)
            print('')
            print('Incorrect guess')
            continue

    if '_' in blank_list:
        print('')
        print(f'The mystery word was: {mystery_word}')
        print('')
        print('Sorry! You lose!')
    else:
        print('')
        print(*blank_list)
        print('')
        print('Congratulations! You win!')


if __name__ == "__main__":
    play_game()
