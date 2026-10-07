# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

## 📝 Document Your Experience

**Game purpose:** A number-guessing game built with Streamlit. The player picks a difficulty, guesses a secret number, and gets "Go HIGHER" or "Go LOWER" hints until they win or run out of attempts.

**Bugs found:**
- On even-numbered attempts the secret was converted to a string, so numbers were compared as text (`"9" > "40"`) and hints were wrong. The same guess could give opposite hints on different attempts.
- The attempt counter started at 1 instead of 0, so "Attempts left" was off by one.
- The "Guess a number between 1 and 100" message was hardcoded and wrong for Easy and Hard.
- Score went up on some wrong guesses (known issue, not fixed).

**Fixes applied:**
- Moved `get_range_for_difficulty`, `parse_guess`, `check_guess`, and `update_score` from `app.py` into `logic_utils.py`.
- `check_guess` now always compares two integers and returns the correct hint.
- Removed the even-attempt `str(secret)` conversion in `app.py`.
- Set the initial attempts value to 0.
- The info message now uses the real `low` and `high` range.
- Added pytest tests in `tests/test_game_logic.py`.


## 📸 Demo Walkthrough

1. Start a Normal game: Attempts left shows 8 and the debug panel shows Attempts 0.
2. Secret is 39. I enter 9 → "📈 Go HIGHER!"
3. I enter 9 three more times → "Go HIGHER" every time (before the fix the hint flipped on even attempts).
4. I enter 80 → "📉 Go LOWER!"
5. I enter 39 → "🎉 Correct!", balloons appear, and "You won! The secret was 39. Final score: 5" is shown.


## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.13.15, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/riteshverma/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 4 items

tests/test_game_logic.py ....                                            [100%]

============================== 4 passed in 0.02s ===============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
