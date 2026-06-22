# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

Opening the "Developer Debug Info" tab revealed the secret number, which made it possible to test hints directly against a known answer. The first concrete bug I noticed was that the hints were backwards — when my guess was too high, the game told me "Go HIGHER!", and when it was too low, it said "Go LOWER!", the exact opposite of what I needed. A second bug appeared on Hard mode: the info banner still read "Guess a number between 1 and 100" even though Hard's actual range is 1–50, so the game was lying about the valid input range. Switching difficulty mid-game also did not reset the secret number, meaning a secret like 75 from Normal mode would carry over into Hard mode (which only goes to 50), making that round impossible to win. Finally, the "New Game" button was broken. Once you successfully made a guess, instead of pressing New Game, you would have to refresh the whole page making that function completely useless

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess:47|"Go HIGHER! " hint| GO LOWER! Hint| none
|Selected Hardmode| It shoulod say guess between 1 & 50|It said guess bewtween 1 & 100| none 
|Click NewGame after finished round|Game should reset and start new game|Nothing occured| none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

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
