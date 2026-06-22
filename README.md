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

- [x] **Game's purpose:** A Streamlit number-guessing game where the player tries to guess a secret number within a limited number of attempts. The game gives directional hints after each guess and tracks a running score across the session.
- [x] **Bugs found:** The hint messages were backwards — guessing too high showed "Go HIGHER!" and guessing too low showed "Go LOWER!". The New Game button didn't reset `session_state.status`, so after winning or losing the game stayed frozen and required a full page refresh. The info banner always showed "1 and 100" even on Hard mode (which only goes to 50). On every even-numbered attempt, the secret number was silently converted to a string, which could break the comparison.
- [x] **Fixes applied:** Moved all game logic into `logic_utils.py` and imported it in `app.py`. Fixed `check_guess` so "Too High" correctly maps to "Go LOWER!" and "Too Low" maps to "Go HIGHER!". Added `st.session_state.status = "playing"` to the New Game handler so the game resets properly. Updated the info banner to use the actual `{low}` and `{high}` range from the selected difficulty. Removed the even-attempt type conversion bug.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Select a difficulty from the sidebar (Easy: 1–20, Normal: 1–100, Hard: 1–50)
2. The game generates a secret number within the selected difficulty range
3. Read the info banner to confirm the correct range for your difficulty
4. Enter a number guess in the text box and click Submit Guess
5. If your guess is too low, the game returns "Go HIGHER!"
6. If your guess is too high, the game returns "Go LOWER!"
7. Score updates after each guess — correct guesses earn points, wrong guesses deduct points
8. If you switch difficulty mid-game, the secret number resets to a value within the new range
9. Continue guessing until you either guess correctly or run out of attempts
10. If you guess correctly, balloons appear and your final score is displayed
11. Click New Game to reset — a new secret number generates within the current difficulty range
12. If you run out of attempts, the secret number is revealed and the game ends

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts =============================
tests/test_game_logic.py::test_winning_guess PASSED                      [ 20%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 40%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 60%]
tests/test_game_logic.py::test_hint_too_high_not_too_low PASSED          [ 80%]
tests/test_game_logic.py::test_hint_too_low_not_too_high PASSED          [100%]
============================== 5 passed in 0.06s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
