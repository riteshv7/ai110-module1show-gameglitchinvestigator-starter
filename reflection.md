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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
