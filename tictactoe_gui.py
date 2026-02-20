import tkinter as tk

def make_board(piece_A, piece_B):
    board = [" "] * 9
    for i in piece_A:
        board[i-1] = "A"
    for i in piece_B:
        board[i-1] = "B"
    return board

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

def minimax(piece_A, piece_B, is_ai_turn):
    board = make_board(piece_A, piece_B)
    if win(board):
        if is_ai_turn:
            return -1
        else:
            return 1
    if len(piece_A) + len(piece_B) == 9:
        return 0
    if is_ai_turn:
        best_score = -999
        for i in range(1, 10):
            if i not in piece_A and i not in piece_B:
                piece_B.append(i)
                score = minimax(piece_A, piece_B, False)
                piece_B.pop()
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = 999
        for i in range(1, 10):
            if i not in piece_A and i not in piece_B:
                piece_A.append(i)
                score = minimax(piece_A, piece_B, True)
                piece_A.pop()
                best_score = min(best_score, score)
        return best_score

def get_best_move(piece_A, piece_B):
    best_score = -999
    best_move = None
    for i in range(1, 10):
        if i not in piece_A and i not in piece_B:
            piece_B.append(i)
            score = minimax(piece_A, piece_B, False)
            piece_B.pop()
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

#GUI
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("井字棋 AI")
        self.piece_A = []
        self.piece_B = []
        self.buttons = []
        self.status = tk.Label(root, text="A 的回合", font=("Arial", 14))
        self.status.pack(pady=10)
        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)
        for i in range(9):
            btn = tk.Button(self.frame,
                            text=" ",
                            font=("Arial", 24),
                            width=5,
                            height=2,
                            command=lambda i=i: self.player_move(i))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
        self.reset_btn = tk.Button(root, text="重新開始", command=self.reset)
        self.reset_btn.pack(pady=10)

    def player_move(self, index):
        pos = index + 1
        if pos in self.piece_A or pos in self.piece_B:
            return
        self.piece_A.append(pos)
        self.update_board()
        result = self.check_game_over()
        if result == "win":
            self.status.config(text="A Win.")
            self.disable_all()
            return
        if result == "tie":
            self.status.config(text="Tie.")
            return
        self.status.config(text="AI Thinking...")
        self.root.after(300, self.ai_move)

    def ai_move(self):
        pos = get_best_move(self.piece_A, self.piece_B)
        self.piece_B.append(pos)
        self.update_board()
        result = self.check_game_over()
        if result == "win":
            self.status.config(text="AI Win.")
            self.disable_all()
            return
        if result == "tie":
            self.status.config(text="Tie.")
            return
        self.status.config(text="A 的回合")

    def check_game_over(self):
        board = make_board(self.piece_A, self.piece_B)
        if win(board):
            return "win"
        if len(self.piece_A) + len(self.piece_B) == 9:
            return "tie"
        return None

    def update_board(self):
        board = make_board(self.piece_A, self.piece_B)
        for i in range(9):
            self.buttons[i].config(text=board[i])

    def disable_all(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset(self):
        self.piece_A = []
        self.piece_B = []
        for btn in self.buttons:
            btn.config(text=" ", state="normal")
        self.status.config(text="A 的回合")

#啟動
root = tk.Tk()
game = TicTacToeGUI(root)
root.mainloop()