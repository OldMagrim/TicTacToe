# Давайте создадим простую игру "Крестики-нолики" (Tic-Tac-Toe) для консоли. Мы реализуем следующие функции:

# 1) Функция для отображения текущего состояния игрового поля.
# 2) Функция для проверки завершенности игры.
# 3) Проверка корректности ввода пользователем координат для хода.
# 4) Простое взаимодействие с пользователем через консоль.

# Вот пример реализации:

def print_board(board):
    """
    Функция отображает текущее состояние игрового поля.
    """
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def check_winner(board):
    """
    Функция проверяет, есть ли победитель или ничья.
    """
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    # Проверка на ничью
    if all(cell != ' ' for row in board for cell in row):
        return 'Draw'

    # Игра продолжается
    return None

def is_valid_move(board, row, col):
    """
    Функция проверяет корректность ввода координат для хода.
    """
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def main():
    """
    Основная функция для взаимодействия с пользователем и управления игрой.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Игрок {current_player}, введите ваш ход (ряд + столбец через пробел): ").split()

        if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
            print("Некорректный ввод. Пожалуйста, введите два числа, разделенные пробелом.")
            continue

        row, col = map(int, move)

        if not is_valid_move(board, row, col):
            print("Некорректный ход. Ячейка занята или координаты вне диапазона.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == 'Draw':
                print("Игра окончена. Ничья.")
            else:
                print(f"Игрок {winner} победил!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
