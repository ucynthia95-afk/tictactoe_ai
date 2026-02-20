def Board(piece_A, piece_B):
    board = [" "]*9
    for i in piece_A:
        board[i-1] = "A"
    for i in piece_B:
        board[i-1] = "B"
    return board

def Board_print(board):
    for i in range(9):
        print(" ", end="")
        if board[i] == " ":
            print(" ", end=" ")
        else:
            print(board[i], end=" ")
        if i % 3 != 2:
            print("|",end="")
        else:
            print()

def win(board):
    for i in range(3):
        if board[3*i] != " " and board[3*i] == board[3*i+1] == board[3*i+2]:
            return True
        if board[i] != " " and board[i] == board[3+i] == board[6+i]:
            return True
    if board[0] != " " and board[0] == board[4] == board[8]:
        return True
    if board[2] != " " and board[2] == board[4] == board[6]:
        return True
    return False

def main():
    piece_A = []
    piece_B = []
    for i in range(9):
        if i % 2 == 0:
            chess = "A"
            while True:
                piece_input = int(input("A 輸入位置(1-9): "))
                if piece_input < 1 or piece_input > 9:
                    print("超出範圍，請重新輸入")
                    continue
                if piece_input in piece_A or piece_input in piece_B:
                    print("該位置已被下過，請重新輸入")
                    continue
                piece_A.append(piece_input)
                break
        else:
            chess = "B"
            while True:
                piece_input = int(input("B 輸入位置(1-9): "))
                if piece_input < 1 or piece_input > 9:
                    print("超出範圍，請重新輸入")
                    continue
                if piece_input in piece_B or piece_input in piece_A:
                    print("該位置已被下過，請重新輸入")
                    continue
                piece_B.append(piece_input)
                break
        board = Board(piece_A, piece_B)
        Board_print(board)
        if win(board):
            print(chess, "Win.")
            break
        if i == 8:
            print("Tie.")

if __name__ == "__main__":
    main()