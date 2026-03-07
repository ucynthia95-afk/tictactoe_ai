# 井字棋 AI (Tic-Tac-Toe AI)

結合 **Minimax 演算法**與 **Q-Learning 強化學習**的井字棋 AI 專案。

 **線上試玩：** https://ucynthia95-afk.github.io/tictactoe_ai/tictactoe_ai.html

---

## 專案結構

| 檔案 | 說明 | 開發方式 |
| --- | --- | --- |
| `tictactoe.py` | Python 終端機版（人 vs AI） | **自己實作** |
| `tictactoe_gui.py` | Python tkinter GUI 版 | **自己實作** |
| `analysis.py` | AI 效能分析工具 | **自己實作** |
| `tictactoe_ai.html` | 網頁版（含 AI vs AI、Q-Learning 訓練） | LLM 輔助開發 |

---

## 功能特色

### 核心功能（自主開發）
* **Minimax 演算法實作**：完整的博弈樹搜尋與最優解計算
* **Alpha-Beta 剪枝優化**：減少不必要的節點評估，提升效率
* **終端機互動介面**：清晰的棋盤顯示與輸入驗證
* **GUI 圖形化介面**：使用 tkinter 建立友善的使用者介面
* **效能分析系統**：自動化測試 AI 勝率與決策時間

### 延伸功能（LLM 輔助）
* Q-Learning 強化學習實作
* 網頁版互動介面
* AI vs AI 對戰模式
* 即時訓練與勝率統計

---

## 執行方式

### 終端機版（核心版本）
```bash
python tictactoe.py
```

### GUI 圖形介面版
```bash
python tictactoe_gui.py
```
需要：`tkinter`（Python 內建）

### 效能分析工具
```bash
python analysis.py
```
執行 100 場測試，分析 AI 表現

### 網頁版
直接用瀏覽器開啟 `tictactoe_ai.html`，或前往：
https://ucynthia95-afk.github.io/tictactoe_ai/tictactoe_ai.html

---

## 技術說明

### Minimax 演算法（自主實作）

Minimax 是一種用於雙人零和遊戲的決策演算法。核心概念：

1. **遞迴建立博弈樹**：模擬所有可能的走法
2. **評估終止狀態**：贏 +10、輸 -10、平手 0
3. **回溯最優解**：最大化玩家選擇最大分數，最小化玩家選擇最小分數

```python
def minimax(self, depth, is_maximizing, alpha, beta):
    winner = self.check_winner()
    
    # 終止狀態評估
    if winner == 'O':  return 10 - depth  # AI 贏，深度越淺分數越高
    if winner == 'X':  return depth - 10  # 人類贏
    if winner == 'Draw': return 0         # 平手
    
    if is_maximizing:  # AI 回合
        max_eval = float('-inf')
        for row, col in self.get_available_moves():
            self.board[row][col] = 'O'
            eval_score = self.minimax(depth + 1, False, alpha, beta)
            self.board[row][col] = ' '
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:  # Alpha-Beta 剪枝
                break
        return max_eval
    else:  # 對手回合
        # ... 類似邏輯，但取最小值
```

**重要優化：**
- **深度懲罰**：`10 - depth` 讓 AI 偏好更快獲勝的路徑
- **Alpha-Beta 剪枝**：提早終止不必要的分支搜尋

### Alpha-Beta 剪枝

透過維護 alpha（最大值下界）和 beta（最小值上界），當 `beta <= alpha` 時可以安全地剪枝。

**效能提升：**
- 最壞情況：O(b^d) → 與 Minimax 相同
- 最佳情況：O(b^(d/2)) → 減少約一半的節點評估
- 井字棋實測：從評估 ~5,000 節點降至 ~500 節點

### Q-Learning 強化學習（LLM 輔助實作）

使用 Bellman 方程更新 Q 值：
```
Q(s,a) ← Q(s,a) + α[r + γ·max Q(s') - Q(s,a)]
```

參數設定：
- 學習率 α = 0.3
- 折扣率 γ = 0.9
- 探索率 ε：1.0 → 0.05（逐漸衰減）

---

## 效能測試結果

執行 `python analysis.py` 的實測結果：

```
==================================================
SIMULATION RESULTS (100 games)
==================================================
Total Games Played: 100
Average Time per Game: 0.0385 seconds

Outcomes:
  Minimax AI Wins: 86 (86.0%)
  Random AI Wins:  0 (0.0%)
  Draws:           14 (14.0%)

Analysis:
  ✓ Minimax AI never lost - perfect play achieved!
  ✓ Minimax AI demonstrates strong performance (>80% win rate)
==================================================
```

**發現與結論：**
1. **100% 不敗率**：AI 從未輸給隨機對手
2. **86% 勝率**：大部分情況下獲勝
3. **14% 平手率**：當隨機對手偶然下出最佳解
4. **高效決策**：平均每步僅需 0.04 秒

---

## 學習心得與收穫

### 技術能力提升
1. **演算法理解**：從理論到實作，深刻理解 Minimax 的運作原理
2. **優化技巧**：學會使用 Alpha-Beta 剪枝提升效能
3. **程式架構**：設計可重用的類別結構（TicTacToe class）
4. **測試思維**：開發自動化測試工具驗證演算法正確性
5. **GUI 開發**：學習 tkinter 事件驅動程式設計

### 遇到的挑戰
1. **遞迴邏輯**：一開始難以理解 minimax 的遞迴結構，透過畫出博弈樹才理解
2. **評分函數**：如何設計合理的評分系統（加入深度懲罰）
3. **除錯困難**：AI 下錯棋時不易追蹤問題，透過 print 調試逐步解決

### 對 AI 的新認識
- AI「智慧」的本質是**窮舉式搜尋** + **評估函數**
- 剪枝等優化技巧能大幅提升實用性
- 簡單問題（井字棋）可以達到完美解，但複雜問題（圍棋）需要更高級的方法

---

## 背景說明

這是我為了準備中研院資訊所暑期實習申請而進行的自主學習專案。目標是：

1. 深入理解 AI 基礎演算法（Minimax）
2. 實際動手實作，而非只讀理論
3. 學習如何測試和驗證演算法正確性
4. 展現自主學習能力和研究熱忱

雖然網頁版使用了 LLM 輔助開發，但核心的 Python 實作（終端機版、GUI 版、效能分析）都是我自己從零開始寫的。這個過程讓我對 AI 演算法有了更深的理解，也確認了我想在這個領域深入研究的決心。

---

## 參考資料

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- [Alpha-Beta Pruning - Wikipedia](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning)
- [Q-Learning - Wikipedia](https://en.wikipedia.org/wiki/Q-learning)

---

## 作者

**尤舒筠**
- 就讀：國立臺北科技大學 電資學士班 一年級
- GitHub: [@ucynthia95-afk](https://github.com/ucynthia95-afk)
- Email: [exit137shuyunyu@gmail.com]

---

## 授權

本專案採用 MIT License 授權，歡迎學習與交流使用。

---

## 未來規劃

- [ ] 實作更進階的搜尋演算法（Monte Carlo Tree Search）
- [ ] 擴展到更複雜的棋類遊戲（五子棋、黑白棋）（正在進行五子棋專案，預計透過 C 語言代替 Python 執行核心程式）
- [ ] 深入研究深度強化學習（Deep Q-Network）
- [ ] 優化 GUI 介面與使用者體驗

---

**最後更新：2026年3月**

*這個專案記錄了我從零開始學習 AI 演算法的歷程。每一行程式碼都是我對 AI 領域探索的見證。*
