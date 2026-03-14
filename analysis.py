"""
井字棋 AI 效能分析工具
Tic-Tac-Toe AI Performance Analysis Tool

這個獨立的分析工具測試 Minimax 演算法的效能，
不需要匯入其他檔案即可執行。
"""

import random
import time
from typing import List, Tuple, Optional


class SimpleTicTacToe:
    """簡化的井字棋類別，用於效能測試"""
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
    
    def is_valid_move(self, row: int, col: int) -> bool:
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '
    
    def make_move(self, row: int, col: int, player: str):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False
    
    def check_winner(self) -> Optional[str]:
        # 檢查橫排
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        # 檢查直排
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        # 檢查對角線
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        # 檢查平手
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Draw'
        return None
    
    def get_available_moves(self) -> List[Tuple[int, int]]:
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
    
    def minimax(self, depth: int, is_maximizing: bool, alpha: float, beta: float) -> int:
        winner = self.check_winner()
        
        if winner == 'O': return 10 - depth
        elif winner == 'X': return depth - 10
        elif winner == 'Draw': return 0
        
        if is_maximizing:
            max_eval = float('-inf')
            for row, col in self.get_available_moves():
                self.board[row][col] = 'O'
                eval_score = self.minimax(depth + 1, False, alpha, beta)
                self.board[row][col] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for row, col in self.get_available_moves():
                self.board[row][col] = 'X'
                eval_score = self.minimax(depth + 1, True, alpha, beta)
                self.board[row][col] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval
    
    def get_best_move(self) -> Tuple[int, int]:
        best_score = float('-inf')
        best_move = None
        
        for row, col in self.get_available_moves():
            self.board[row][col] = 'O'
            score = self.minimax(0, False, float('-inf'), float('inf'))
            self.board[row][col] = ' '
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move


class PerformanceAnalyzer:
    """AI 效能分析器"""
    
    def __init__(self):
        self.results = {
            'minimax_wins': 0,
            'random_wins': 0,
            'draws': 0,
            'total_games': 0,
            'total_time': 0
        }
    
    def play_game(self, ai_first: bool = True) -> str:
        game = SimpleTicTacToe()
        current_player = 'O' if ai_first else 'X'
        
        while True:
            if current_player == 'O':
                row, col = game.get_best_move()
                game.make_move(row, col, 'O')
            else:
                available = game.get_available_moves()
                if available:
                    row, col = random.choice(available)
                    game.make_move(row, col, 'X')
            
            winner = game.check_winner()
            if winner:
                if winner == 'O': return 'minimax'
                elif winner == 'X': return 'random'
                else: return 'draw'
            
            current_player = 'X' if current_player == 'O' else 'O'
    
    def run_simulation(self, num_games: int = 100):
        print(f"\n{'='*60}")
        print("井字棋 AI 效能分析 | Tic-Tac-Toe AI Performance Analysis")
        print(f"{'='*60}\n")
        print(f"執行 {num_games} 場測試...")
        print("Minimax AI (O) vs 隨機 AI (X)\n")
        
        start_time = time.time()
        
        for i in range(num_games):
            ai_first = (i % 2 == 0)
            winner = self.play_game(ai_first)
            
            self.results['total_games'] += 1
            if winner == 'minimax':
                self.results['minimax_wins'] += 1
            elif winner == 'random':
                self.results['random_wins'] += 1
            else:
                self.results['draws'] += 1
            
            if (i + 1) % 20 == 0:
                print(f"已完成 {i + 1}/{num_games} 場...")
        
        self.results['total_time'] = time.time() - start_time
        self.print_results()
    
    def print_results(self):
        total = self.results['total_games']
        
        print(f"\n{'='*60}")
        print("測試結果 (Test Results)")
        print(f"{'='*60}")
        print(f"總場次 (Total Games): {total}")
        print(f"總時間 (Total Time): {self.results['total_time']:.2f} 秒")
        print(f"平均每場時間 (Avg Time/Game): {self.results['total_time']/total:.4f} 秒")
        
        print(f"\n結果統計 (Outcomes):")
        print(f"  Minimax AI 獲勝:  {self.results['minimax_wins']:3d} 場 ({self.results['minimax_wins']/total*100:5.1f}%)")
        print(f"  隨機 AI 獲勝:     {self.results['random_wins']:3d} 場 ({self.results['random_wins']/total*100:5.1f}%)")
        print(f"  平手:            {self.results['draws']:3d} 場 ({self.results['draws']/total*100:5.1f}%)")
        
        print(f"\n效能分析 (Performance Analysis):")
        
        if self.results['random_wins'] == 0:
            print("  ✓ Minimax AI 從未輸過 - 達成完美表現！")
            print("  ✓ Perfect play achieved - AI never lost!")
        
        if self.results['minimax_wins'] > total * 0.8:
            print("  ✓ Minimax AI 勝率超過 80% - 表現優異")
            print("  ✓ Win rate > 80% - Excellent performance")
        
        win_rate = self.results['minimax_wins'] / total * 100
        print(f"\n  最終勝率 (Final Win Rate): {win_rate:.1f}%")
        print(f"  不敗率 (Undefeated Rate): {(total - self.results['random_wins'])/total*100:.1f}%")
        
        print(f"{'='*60}\n")


def main():
    print("\n井字棋 Minimax AI 效能測試工具")
    print("Tic-Tac-Toe Minimax AI Performance Testing Tool\n")
    print("本工具將測試 Minimax 演算法（含 Alpha-Beta 剪枝）的效能\n")
    
    analyzer = PerformanceAnalyzer()
    
    print("【快速測試 Quick Test】")
    analyzer.run_simulation(10)
    
    print("\n\n【完整測試 Full Test】")
    analyzer = PerformanceAnalyzer()
    analyzer.run_simulation(100)
    
    print("\n重要發現 (Key Findings):")
    print("─" * 60)
    print("1. Minimax + Alpha-Beta 剪枝確保最佳策略")
    print("2. AI 在最佳情況下從不會輸")
    print("3. 大部分對局以平手結束（當雙方都下最佳解）")
    print("4. 平均決策時間展現演算法效率")
    print("─" * 60)
    print("\n測試完成！Test completed!\n")


if __name__ == "__main__":
    main()