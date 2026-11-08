# COMP1117 Midterm 2026-27: The Palindrome Finder

**Monday 9 November. 45 minutes. 10% of your course mark.**

## Overview

A note-taking app wants a small feature. The user types a note. The app lists the palindromes in the note.

A **palindrome** is a word that reads the same forwards and backwards, such as `level`, `noon` or `121`.

You build this program with the course AI tutor. The program is in `palindromes.py`. Most of it is written. It has 8 gaps, Q1 to Q8. For each gap, the tutor has offered four versions, A to D. Exactly one version is correct. You choose it.

## Description

### Reading the note

The program reads lines with `input()` until the user enters a blank line. The blank line is not part of the note. The lines are joined into one string, with `"\n"` after each line.

### Cleaning

The program looks at each character of the note.

- A letter or a digit is kept, in lower case.
- Every other character becomes one space. This includes spaces, punctuation such as `,` `!` `'` `-`, and the `"\n"` at the end of each line.

### Words

The cleaned note is split into words at the spaces. A word with only 1 character is not a word for this program. Only words with **2 or more** characters are kept.

### Palindromes

A word is a palindrome if its first and last characters are the same, its second and second-last characters are the same, and so on. The program checks each pair with two positions, `left` and `right`, which start at the two ends of the word and move towards each other.

### Output

Before it reads the note, the program prints this line (it is already in `main()`):

```
Type your note. Press Enter on an empty line to finish.
```

After the note, the program prints one answer line:

- each palindrome **once**, in the order it **first** appears in the note, separated by `", "` (a comma and a space);
- or `(none)` if the note has no palindromes.

Your answer line must match the answer line in the examples below exactly: the same words, in the same order, with the same commas and spaces. The lines you type also appear on the screen, but they are not part of the answer.

## Examples

Run the program with `python3 palindromes.py`. On Windows, use `python` or `py` in place of `python3`, here and below. The finished program prints the line above and waits. Type the lines of the note. Press Enter on an empty line to finish. The program then prints its answer line.

**Example 1.** On screen you see:

```
Type your note. Press Enter on an empty line to finish.
Noon: the kayak club.
Kayak at NOON, 7 pm!

noon, kayak
```

Lines 2 to 4 are what you type, ending with the empty line. The last line is the program's answer. Check it against yours.

`noon` and `kayak` each appear twice but are printed once, in the order they first appear. `Noon:` and `NOON,` both become `noon`: the punctuation becomes a space and the letters become lower case. `7` has only 1 character, so it is not a word.

**Example 2.** On screen you see:

```
Type your note. Press Enter on an empty line to finish.
Anna's pop-up shop sold a race
car to Bob. Wow, 11 sales! WOW.

anna, pop, bob, wow, 11
```

Lines 2 to 4 are what you type, ending with the empty line. The last line is the program's answer. Check it against yours.

`Anna's` becomes the words `anna` and `s`, and `pop-up` becomes `pop` and `up`. `race` and `car` are on different lines, so they stay two words. `Wow` and `WOW` both become `wow`. It is printed once, in the place where it first appears. `11` has 2 characters, so it is a word, and it is a palindrome.

**Example 3.** On screen you see:

```
Type your note. Press Enter on an empty line to finish.
Hello there, world.

(none)
```

Lines 2 and 3 are what you type, ending with the empty line. The last line is the program's answer. Check it against yours.

No word in this note is a palindrome, so the program prints `(none)`.

## How to answer

1. Open `palindromes.py` in VS Code.
2. Each gap looks like this:

   ```python
       ## ===== Q4: where left and right start. Uncomment ONE option =====
       ## --- Option A ---
       # left = 1
       # right = -1
       ## --- Option B ---
       ...
       ## ===== end of Q4 =====
   ```

3. Choose one option. Select only its lines, not the `##` label, and press **Ctrl+/** (**Cmd+/** on a Mac). The `#` disappears and the code becomes active. If a `##` label is caught in the selection by mistake, no harm is done: it stays a comment.
4. Uncomment exactly **one** option in each gap. To change your mind, select the lines again and press Ctrl+/ to comment them out.
5. Do not change any other line. Leave the `pass  # placeholder` lines in the gaps where they are. (The bonus is different: there you replace its placeholder line with your own code.)
6. Run `python3 check.py`. It tells you if a gap has no option or more than one. It does not tell you if a choice is right.
7. You may run `python3 palindromes.py` at any time, and test it with the examples above or your own notes. The file runs even before you choose anything. The first line always appears. Until you answer Q1, the program does not read a note: it prints the first line and finishes at once. Until you answer Q8, it prints no answer line.

## Bonus (20 marks)

Near the end of `palindromes.py` is `is_palindrome_rec(word, left, right)`. Write it yourself, using recursion. The function returns `True` if the characters from position `left` to position `right` read the same forwards and backwards, and `False` if not.

Do the bonus without any AI. The course AI tutor will not help with it. If your tutor record shows that you asked the tutor for help with the bonus, the bonus scores 0.

The bonus has strict rules. The marking script checks every rule, and its decision is final.

1. **All or nothing.** The bonus is worth 20 marks or 0. There is no partial credit.
2. **Fixed first line.** Keep `def is_palindrome_rec(word, left, right):` exactly as it is. The function is tested only as `is_palindrome_rec(word, 0, len(word) - 1)`.
3. **Every hidden test must pass.** The tests include the empty word (`left` is 0 and `right` is -1), a word of one letter, words of even and odd length, words that differ at the ends, words that differ in the middle, and words made of digits.
4. **Real two-position recursion.** Each call compares at most one pair, `word[left]` and `word[right]`, and then calls `is_palindrome_rec(word, left + 1, right - 1)`. The script counts the calls. A palindrome must take about half its length in calls. A word that is not a palindrome must stop at the first pair that does not match.
5. **Not allowed inside the function:**
   - `for` or `while` loops, and list comprehensions;
   - slicing, such as `word[1:]` or `word[::-1]`, and `reversed()`;
   - comparing the whole word at once, such as `word == ...`;
   - calling any function except `is_palindrome_rec` itself and `len`;
   - `global` or `nonlocal`;
   - a function defined inside the function;
   - default values for the parameters.
6. **Only this function counts.** Helper functions earn nothing. If you change the first line, or change anything else in the file for the bonus (for example, a test line left in the file), the bonus is 0. You may add test lines while you work, but remove them all before you submit. To test the function, put a test line such as `print(is_palindrome_rec("level", 0, 4))` just above the line `main()` at the bottom of the file, run the file, and then delete the test line before you submit. Your choices in the gaps are allowed, of course.
7. **The main program must still work.** If `check.py` reports a problem, or the file crashes when it runs, the bonus is 0.
8. **The marking script decides.** A case it cannot classify is checked by a person, and is not awarded automatically.

## Marks

- Q1 to Q8: 12.5 marks each, 100 marks in total.
- Bonus: 20 extra marks on top of the 100, all or nothing, under the rules in the Bonus section. With the bonus, the highest possible mark is 120.
- The midterm is worth 10% of your course mark: 100 marks gives the full 10%, and the bonus can add up to 2 more percentage points (12% in all).
- Your choices are also run on hidden notes, beyond the examples above.
- There is no penalty for a wrong choice. Choose an option in every gap.

## How to submit

1. Run `python3 check.py` and fix anything it reports.
2. On Ed, open the lesson **Midterm** and upload `palindromes.py`.
3. Submit before the end of the sitting. There are no late submissions. You may submit more than once: your last submission counts.

You will not see your mark during the sitting. Marks are released after both subclasses have sat the midterm.

## Rules for the sitting

- **The course AI tutor:** allowed for Q1 to Q8 only. It is asked to explain the options and to hear your reasoning before it gives its own view. It has no answer key and can be wrong: checking is your job. It never changes your file. It will not help with the bonus.
- **Other AI tools** (ChatGPT, DeepSeek, Copilot, HKU GenAI and others): not allowed. Using one is cheating, and the whole midterm scores 0.
- **Closed book, except the course AI tutor:** notes, slides, Ed lessons and the Python documentation are not allowed. Use Ed only to submit in the lesson **Midterm**.
- **Talking to other students, or sharing the questions:** not allowed during the sitting.

## Before the clock starts

1. Clone this repository and open the folder in VS Code.
2. Run `python3 check.py` (on Windows, `python check.py` or `py check.py`). It should say that every gap still needs an option.
3. Run `python3 palindromes.py`. It should print `Type your note. Press Enter on an empty line to finish.` and then finish at once, because Q1 is not answered yet, so it reads no note. Once Q1 is answered, the program waits for your note: type its lines, then press Enter on an empty line to finish.
