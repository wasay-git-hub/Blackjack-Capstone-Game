# 🃏 Blackjack Capstone Project

A Python console-based Blackjack game where you play against the computer (dealer). Built as a capstone project with simple logic, random card drawing, and optional Ace handling.

---

## 📌 Features

- Play against a computer dealer.
- Cards are drawn randomly using Python's `random` module.
- Aces are handled smartly — treated as `11` or `1` based on score.
- Score tracking and bust conditions.
- Option to play multiple rounds.
- Clean, console-friendly output.

---

## 🕹️ How to Play

### Game Start:
- Both player and computer start with two cards.
- The player sees both of their cards and only one of the dealer’s.

### Your Turn:
- You choose to:
  - **`y`** → *Hit*: draw another card
  - **`n`** → *Stand*: end your turn and let the dealer play
- If your score goes over 21 and an Ace is present, the Ace becomes 1.
- If the score still exceeds 21 → **BUST**, you lose.

### Dealer's Turn:
- The dealer (computer) reveals the hidden card.
- It **keeps drawing** until the total score is **17 or higher**.
- Dealer busts if score > 21 (unless an Ace is converted).

---

## 🎮 Game Rules (Simplified Blackjack)

| Rule                     | Details                                       |
|--------------------------|-----------------------------------------------|
| Card Values              | 2–10 = face value, J/Q/K = 10, Ace = 11 or 1 |
| Blackjack                | Not explicitly handled (just regular scoring) |
| Win Condition            | Closest to 21 without going over              |
| Dealer Draw Rule         | Dealer draws until score is 17 or more       |
| Bust                     | Score exceeds 21                              |
| Draw                     | Equal scores                                  |
| Multiple Rounds          | Supported with prompt after each match       |

---

