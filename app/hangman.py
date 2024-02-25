from random import randint


def read_word_list(words_file):
    word_list = []
    file = open(f"app/data/{words_file}", "r")
    for line in file:
        word_list.append(line.strip())
    return word_list


def choose_word(word_list):
    index = randint(0, len(word_list) - 1)
    return word_list[index]


# def start_game():

#     # chosing random word
#     words = read_word_list()
#     chosen_word = choose_word(words)
#     return chosen_word


def print_board(board):
    return "".join(board)


def check_board(letter, board, word, lives):
    looses_life = True
    for i in range(len(word)):
        if letter == word[i]:
            board[i] = letter
            looses_life = False
    if looses_life and lives > 0:
        lives -= 1

    if word == "".join(board):
        return board, lives, 1

    return board, lives, 0


def guess_letter():
    print("guess letter")
