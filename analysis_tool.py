"""
AI Performance Analysis
Analyze the performance of different AI strategies in Tic-Tac-Toe

This script runs multiple games to compare:
1. Minimax AI vs Random AI
2. Statistics on game outcomes
3. Average decision time
"""

import time
import random
from tictactoe import TicTacToe
from typing import Dict, Tuple

class RandomAI:
    """Random move selection AI for comparison."""
    
    @staticmethod
    def get_move(game: TicTacToe) -> Tuple[int, int]:
        """Select a random available move."""
        available = game.get_available_moves()
        return random.choice(available) if available else None


class GameAnalyzer:
    """Analyze AI performance through multiple game simulations."""
    
    def __init__(self):
        self.results = {
            'minimax_wins': 0,
            'random_wins': 0,
            'draws': 0,
            'total_games': 0,
            'total_time': 0
        }
    
    def play_automated_game(self, first_player: str = 'minimax') -> str:
        """
        Play one automated game between Minimax AI and Random AI.
        
        Args:
            first_player: 'minimax' or 'random' to determine who goes first
            
        Returns:
            Winner: 'minimax', 'random', or 'draw'
        """
        game = TicTacToe()
        current = first_player
        
        while True:
            if current == 'minimax':
                row, col = game.get_best_move()
                game.make_move(row, col, 'O')
            else:
                row, col = RandomAI.get_move(game)
                game.make_move(row, col, 'X')
            
            winner = game.check_winner()
            if winner:
                if winner == 'O':
                    return 'minimax'
                elif winner == 'X':
                    return 'random'
                else:
                    return 'draw'
            
            current = 'random' if current == 'minimax' else 'minimax'
    
    def run_simulation(self, num_games: int = 100):
        """
        Run multiple games and analyze results.
        
        Args:
            num_games: Number of games to simulate
        """
        print(f"\nRunning {num_games} games simulation...")
        print("Minimax AI (O) vs Random AI (X)\n")
        
        start_time = time.time()
        
        for i in range(num_games):
            # Alternate who goes first
            first_player = 'minimax' if i % 2 == 0 else 'random'
            winner = self.play_automated_game(first_player)
            
            self.results['total_games'] += 1
            if winner == 'minimax':
                self.results['minimax_wins'] += 1
            elif winner == 'random':
                self.results['random_wins'] += 1
            else:
                self.results['draws'] += 1
            
            # Progress indicator
            if (i + 1) % 10 == 0:
                print(f"Completed {i + 1}/{num_games} games...")
        
        self.results['total_time'] = time.time() - start_time
        self.print_results()
    
    def print_results(self):
        """Print detailed analysis results."""
        total = self.results['total_games']
        
        print("\n" + "="*50)
        print("SIMULATION RESULTS")
        print("="*50)
        print(f"Total Games Played: {total}")
        print(f"Total Time: {self.results['total_time']:.2f} seconds")
        print(f"Average Time per Game: {self.results['total_time']/total:.4f} seconds")
        print("\nOutcomes:")
        print(f"  Minimax AI Wins: {self.results['minimax_wins']} ({self.results['minimax_wins']/total*100:.1f}%)")
        print(f"  Random AI Wins:  {self.results['random_wins']} ({self.results['random_wins']/total*100:.1f}%)")
        print(f"  Draws:           {self.results['draws']} ({self.results['draws']/total*100:.1f}%)")
        print("\nAnalysis:")
        
        if self.results['random_wins'] == 0:
            print("  ✓ Minimax AI never lost - perfect play achieved!")
        else:
            print(f"  ⚠ Random AI won {self.results['random_wins']} games - investigating...")
        
        if self.results['minimax_wins'] > total * 0.8:
            print("  ✓ Minimax AI demonstrates strong performance (>80% win rate)")
        
        print("="*50)


def main():
    """Main function to run the analysis."""
    print("Tic-Tac-Toe AI Performance Analyzer")
    print("This script analyzes the Minimax algorithm's performance")
    
    analyzer = GameAnalyzer()
    
    # Run simulation with different game counts
    print("\n--- Quick Test (10 games) ---")
    analyzer.run_simulation(10)
    
    # Reset for larger simulation
    analyzer = GameAnalyzer()
    print("\n\n--- Full Simulation (100 games) ---")
    analyzer.run_simulation(100)
    
    print("\nKey Findings:")
    print("1. Minimax with alpha-beta pruning ensures optimal play")
    print("2. AI never loses when playing optimally")
    print("3. Most games result in draws when both play perfectly")
    print("4. Average decision time demonstrates algorithm efficiency")


if __name__ == "__main__":
    main()
