import random
import os


with open('words.txt') as my_file:
    read_file = my_file.read()
word_list = read_file.split()
easy_list = []
medium_list = []
hard_list = []
for word in word_list:
    if len(word) in range(4, 7):
        easy_list.append(word)
    elif len(word) in range(6, 9):
        medium_list.append(word)
    elif len(word) >= 8:
        hard_list.append(word)


def make_word(level):
    i = 0
    while i == 0:
        if level == 'easy' or level == 'e':
            mystery_word = random.choice(easy_list).upper()
            i += 1
        elif level == 'medium' or level == 'm':
            mystery_word = random.choice(medium_list).upper()
            i += 1
        elif level == 'hard' or level == 'h':
            mystery_word = random.choice(hard_list).upper()
            i += 1
        else:
            print('\n⛔️⚠️ PLEASE ENTER A VALID LEVEL ⚠️ ⛔️')
            level = input('\nLevel: (e)asy / (m)edium / (h)ard: ').lower()
    return mystery_word


def play_game():
    play = True
    while play:
        os.system('clear')
        print('\n❓❔ LET\'S PLAY A GUESSING GAME!❔❓')
        input_level = input('\nLevel: (e)asy / (m)edium / (h)ard: ').lower()

        mystery_word = make_word(input_level)

        unpacked = [*mystery_word]

        blank_list = []
        for letter in mystery_word:
            blank_list.append('_')

        # print(f'\n{mystery_word}')

        guess_count = 0
        guessed_list = []
        incorrect_list = []
        os.system('clear')
        while guess_count < 8 and '_' in blank_list:
            print('\n❓❔ JEROME\'S GUESSING GAME!❔❓')
            if guess_count == 7:
                print('\n⚠️  WARNING: ONE GUESS REMAINING ⚠️\n')
            print('')
            print(*blank_list)
            print(f'\nGuesses remaining: {8 - guess_count}')
            unpack_incorrect = ", ".join(incorrect_list)
            if len(incorrect_list) > 0:
                print(f'\nIncorrect guesses: {unpack_incorrect}')
            guess = input('\nGuess a letter: ').upper()
            os.system('clear')
            if not guess.isalpha() or len(guess) != 1:
                print('\n⛔️⚠️  INVALID GUESS. Please guess one letter. ⚠️ ⛔️ ')
                continue
            elif guess in guessed_list:
                print(f'\n🤦🏽‍♀️ \'{guess}\' has already been guessed! 🤦🏽')
                continue
            elif guess in mystery_word:
                guessed_list.append(guess)
                for i in range(len(blank_list)):
                    if unpacked[i] in guessed_list:
                        blank_list[i] = unpacked[i]
                print(f'\n✅ \'{guess}\' was a good guess! ✅')
                continue
            else:
                guess_count += 1
                guessed_list.append(guess)
                incorrect_list.append(guess)
                print(f'\n❌ \'{guess}\' was a bad guess ❌')

        if '_' in blank_list:
            os.system('clear')
            print(f'\nThe mystery word was: {mystery_word}')
            print('\nSorry! You lose!')
        else:
            os.system('clear')
            print('')
            print(*blank_list)
            print('\n🏆 Congratulations! You win! 🏆')

        good_input = 0
        while good_input == 0:
            play_again = input('\nDo you want to play again? y / n: ').lower()
            if play_again != 'y' and play_again != 'n':
                print('Invalid input')
                continue
            elif play_again == 'y':
                play = True
                good_input += 1
            else:
                play = False
                os.system('clear')
                good_input += 1


if __name__ == "__main__":
    play_game()
