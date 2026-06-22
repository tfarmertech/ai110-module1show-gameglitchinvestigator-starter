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

-Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude and ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). The AI suggestion that was corrected was that the hints were reversed in check_guess. I checked this fixing the bug and testing by saving and running the app, and proceeding to open the developer debug info tab and seeing the result wass now accurate.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Thhe wrong suggestion was that the AI said the hint system was the sole cause of wrong feedback duyring gameplay which was fase. On every even numbered attempt, I realized the code converts the secret number to a string before comparing it to the integer guess.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? If it performed in the way it was intended.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I manually tested the New Game button after fixing it to use random.randint(low, high) instead of the hardcoded random.randint(1, 100). To verify, I switched to Hard mode, clicked New Game, and opened the Developer Debug Info tab to check the generated secret number. This showed me that hardcoded values are an easy bug to miss because the code still runs without errors, while secretly/silently being wrong.

- Did AI help you design or understand any tests? How? Yes. I described the bugs I found to the AI and it helped me understand which ones were worth testing and why. For the New Game bug specifically, the AI pointed out that the hardcoded random.randint(1, 100) ignored the difficulty variable entirely, which helped me know exactly what to check in the Developer Debug Info tab after implementing the fix.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the entire script every time you interact with the page or click a button, type something, anything. That means regular variables reset every time. Session state is a dictionary that persists between those reruns so your game can actually remember things like the secret number, your score, and how many attempts you've made.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Role based prompting. I told my claude to act as a senior developer and it broke everything down in a way I cold understand.
  - This could be a testing habit, a prompting strategy, or a way you used Git.

- What is one thing you would do differently next time you work with AI on a coding task? I accidently had it on bypass permissions instead of plan mode so it almost broke my program. Of course no harm was done since I can copy the original code from the repo, but it definetly was a scare. So moving forward, ill always make sure to double check permissions and monitor all changes.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
It helped me understand some of the limits and strengths of AI generated code. I learned how much role prompting can benefit a person in terms of learning and achieving a goal. Throughout this project, I found ways that can make my work during my internship even more efficient. Thank you CODE PATH! 
