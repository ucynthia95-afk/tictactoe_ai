# 井字棋 AI

結合 **Minimax 演算法**與 **Q-Learning 強化學習**的井字棋 AI 專案。

🎮 **線上試玩：** https://ucynthia95-afk.github.io/tictactoe_ai/tictactoe_ai.html

---

## 專案結構

| 檔案 | 說明 |
|------|------|
| `tictactoe.py` | Python 終端機版（人 vs AI） |
| `tictactoe_gui.py` | Python tkinter GUI 版 |
| `tictactoe_ai.html` | 網頁版（含 AI vs AI、Q-Learning 訓練） |

---

## 功能

- 人 vs AI、人 vs 人、AI vs AI 三種對戰模式
- Minimax + Alpha-Beta 剪枝（最優解，AI 不會輸）
- Q-Learning 自我對弈訓練（可即時在瀏覽器訓練）
- 難度選擇：簡單 / 中等 / 困難 / RL
- 勝率統計與對局紀錄

---

## 執行方式

**終端機版**
```bash
python tictactoe.py
```

**GUI 版**
```bash
python tictactoe_gui.py
```

**網頁版**  
直接用瀏覽器開啟 `tictactoe_ai.html`，或前往上方線上連結。

---

## 技術說明

### Minimax 演算法
AI 下每步前，遞迴模擬所有可能的後續走法，並對結果打分數（贏 +1 / 平 0 / 輸 -1），選擇對自己最有利的那步。搭配 Alpha-Beta 剪枝省略不必要的計算。

### Q-Learning 強化學習
透過自我對弈累積經驗，根據 Bellman 方程式更新每個盤面狀態的行動價值：

```
Q(s,a) ← Q(s,a) + α[r + γ·max Q(s') - Q(s,a)]
```

- 學習率 α = 0.3
- 折扣率 γ = 0.9  
- 探索率 ε 從 1.0 衰減至 0.05

---

## 學到的東西

- 遞迴與博弈樹的概念
- Minimax 與 Alpha-Beta 剪枝的實作
- Q-Learning 的基本原理與 Q-table 更新
- tkinter GUI 事件處理
- Git 版本控制流程
