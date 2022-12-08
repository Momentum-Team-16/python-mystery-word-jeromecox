import random


def play_game():
    play = True
    while play:
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
        while guess_count < 1 and '_' in blank_list:
            print('')
            print(*blank_list)
            print('')
            print(f'Guesses remaining: {8 - guess_count}')
            print('')
            unpack_guessed = [*guessed_list]
            if len(guessed_list) > 0:
                print(f'You have already guessed: {unpack_guessed}')
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
                guessed_list.append(guess)
                for i in range(len(blank_list)):
                    if unpacked[i] in guessed_list:
                        blank_list[i] = unpacked[i]

                print('')
                print('Good guess!')
                print('')

                continue
            else:
                guess_count += 1
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

        good_input = 0
        while good_input == 0:
            print('')
            play_again = input('Do you want to play again? y / n: ').lower()
            if play_again != 'y' and play_again != 'n':
                print('Invalid input')
                continue
            elif play_again == 'y':
                play = True
                good_input += 1
            else:
                play = False
                good_input += 1


if __name__ == "__main__":
    play_game()
