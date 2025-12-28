# Poker Game with GUI

## 📋 Project Overview
A Python-based video poker game implementing two popular poker variants with a fully functional graphical user interface.

## 🎮 Features
- **Two Game Modes**: Jacks or Better & Deuces Wild
- **Interactive Gameplay**: Click cards to hold/discard
- **Real-time Statistics**: Track earnings, hands played, and maximum cash
- **Visual Feedback**: Card inversion system for selection
- **Payout Tables**: In-game reference for hand values
- **Complete Game Logic**: Full hand calculation and validation

## 🏗️ Architecture
- poker_gui.py # Main GUI application
- poker_calc.py # Hand calculation logic
- cards.py # Card/Deck class definitions
- poker_hands_test.py # Unit tests
- inverted.py # Image processing utility
- card_images/ # 52 card PNGs
- inverted_images/ # Inverted card variants

## 🚀 Installation & Usage
```bash
# Clone repository
git clone https://github.com/Javanh06/Poker.git

# Run the game
python3 poker_gui.py

# Run tests
python3 poker_hands_test.py
