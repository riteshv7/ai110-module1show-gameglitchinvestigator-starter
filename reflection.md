# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

### Bug 1: Wrong hint on even-numbered attempts
- **Input/trigger:** Secret was 40. I guessed 60, then 9, then 9 again.
- **Expected:** A guess of 9 should always say to go HIGHER.
- **Actual:** On attempt 4 the game said "Go LOWER!" for a guess of 9.
- **Suspected cause:** In `app.py`, on even attempts the secret is converted with
  `str(...)`, so the comparison happens on text ("9" > "40") instead of numbers.

### Bug 2: Attempt counter starts at 1
- **Input/trigger:** Opened the app and made no guesses.
- **Expected:** Attempts: 0 and "Attempts left: 8" on Normal.
- **Actual:** Debug panel showed Attempts: 1 and the info box said "Attempts left: 7".
- **Suspected cause:** `st.session_state.attempts = 1` in `app.py`.

### Bug 3: Score goes up on wrong guesses
- **Input/trigger:** Three wrong guesses (60, 9, 9) against secret 40.
- **Expected:** Score stays at 0 or goes down.
- **Actual:** Score was 5.
- **Suspected cause:** `update_score` in `app.py` adds +5 for "Too High" on even attempts.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output | Suspected Code Location |
|---|---|---|---|---|
| Secret 40, guess 9 on attempt 4 | "Go HIGHER" | "Go LOWER" | none | `app.py`, `secret = str(...)` on even attempts; `check_guess` |
| Fresh game, no guesses | Attempts 0, 8 left | Attempts 1, 7 left | none | `app.py`, `st.session_state.attempts = 1` |
| Wrong guesses 60, 9, 9 vs secret 40 | Score ≤ 0 | Score 5 | none | `app.py`, `update_score` |

---

## 2. How did you use AI as a teammate?

**Tools used:** I used Claude in the web chat to understand the code and plan the fixes. I also had the VS Code chat panel open but mainly worked from Claude's explanations.

**A correct suggestion:** Claude pointed out that `app.py` converts the secret to a string on even-numbered attempts (`secret = str(st.session_state.secret)`), so Python was comparing numbers as text. That explained why the same guess could give opposite hints. I verified it by guessing 9 four times in a row against a secret of 39 and getting the same hint every time after the fix, and I added a pytest case (`check_guess(9, 50)` must be "Too Low") that would fail with string comparison.

**A suggestion I did not accept as written:** Early on, Claude predicted what hints the buggy game would show for certain guesses, but my real results didn't match that prediction exactly. Instead of trusting it, I reproduced the bug myself, recorded what I actually saw (a guess of 9 gave "Go LOWER!" on attempt 4), and wrote that in my bug log. I also chose to fix only the bugs I could verify and left the scoring bug in `update_score` alone rather than rewriting more code than the task required.

---

## 3. Debugging and testing your fixes

I decided a bug was fixed only when it passed both a test and a manual check. For the hint bug, I ran the live game and submitted 9 repeatedly against a secret of 39, and it said "Go HIGHER" on both odd and even attempts, which is where it used to change. I also ran pytest with four tests (too high, too low, win, and a numeric-vs-string comparison) and got `4 passed`. Plain `pytest` first failed with `ModuleNotFoundError: No module named 'logic_utils'`, and running `python -m pytest` fixed it because it adds the project folder to Python's path. Claude helped me design the tests by suggesting the "9 vs 50" case, which targets the exact string-comparison bug I fixed. The scoring in `update_score` still rewards some wrong guesses, so I know it isn't fully fixed.

---

## 4. What did you learn about Streamlit and state?

Streamlit reruns the whole Python script from top to bottom every time you click a button or type something. Normal variables get reset on every rerun, so a secret number created with `random.randint` would change each time. `st.session_state` is like a small notebook that survives between reruns, so I store the secret, attempts, score, and history there and only create them if they aren't already there (`if "secret" not in st.session_state`). That's why the game remembers my guesses even though the script restarts after each click.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is reproducing a bug and writing down the exact input, expected result, and actual result before asking AI for a fix. That made it easy to tell whether a fix really worked. Next time I would write the pytest test first, before changing the code, so I can see it fail and then pass. This project changed how I think about AI-generated code: it can look clean and still hide logic mistakes, so I now treat it as a draft that I have to test and verify myself.
