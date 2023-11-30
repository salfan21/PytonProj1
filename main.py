from random import randrange


def display_board(board):
    # Функція приймає на вхід поточний стан дошки та виводить його в консоль.
    for row in board:
        print("|".join(map(str, row)))
        print("-" * 5)


def enter_move(board):
    # Функція приймає поточний стан дошки, запитує користувача про його хід,
    # перевіряє введені дані та оновлює дошку відповідно до рішення користувача.
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                raise ValueError("Invalid input. Please enter a number between 1 and 9.")

            row, col = divmod(move - 1, 3)
            if board[row][col] == "O" or board[row][col] == "X":
                raise ValueError("Invalid move. The square is already taken.")

            board[row][col] = "O"
            break
        except ValueError as e:
            print(e)


def make_list_of_free_fields(board):
    # Функція переглядає дошку і будує список всіх вільних квадратів.
    # Список складається з кортежів, кожен кортеж - це пара номерів рядка і стовпця.
    free_fields = [(row, col) for row in range(3) for col in range(3) if
                   board[row][col] != "O" and board[row][col] != "X"]
    return free_fields


def victory_for(board, sign):
    # Функція аналізує стан дошки, щоб перевірити, чи виграв гравець, який використовує 'O' або 'X'.
    # Повертає True, якщо є переможець, і False в іншому випадку.
    for row in board:
        if all(cell == sign for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False


def draw_move(board):
    # Функція робить хід комп'ютера та оновлює дошку.
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        move = randrange(len(free_fields))
        row, col = free_fields[move]
        board[row][col] = "X"


if __name__ == "__main__":
    board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

    display_board(board)

    while True:
        enter_move(board)
        display_board(board)

        if victory_for(board, "O"):
            print("You win!")
            break

        if len(make_list_of_free_fields(board)) == 0:
            print("It's a draw!")
            break

        draw_move(board)
        display_board(board)

        if victory_for(board, "X"):
            print("Computer wins!")
            break