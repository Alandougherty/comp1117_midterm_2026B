# COMP1117 Midterm 2026-27: The Palindrome Finder
#
# Read README.md first. It describes what this program must do.
#
# HOW TO ANSWER
# The program has 8 gaps, Q1 to Q8. Each gap offers four versions, A to D.
# Exactly one version is correct. In each gap, uncomment exactly ONE option:
# select the lines under its "## --- Option X ---" label and press Ctrl+/
# (Cmd+/ on a Mac). Do not uncomment the "##" labels.
#
# - Do not change any other line. Leave the "pass  # placeholder" lines.
# - The file runs at any time, even before you choose anything.
# - Run:  python3 check.py   to check that each gap has exactly one option.
# - The bonus, is_palindrome_rec, is near the end. You write it yourself.

def read_note():
    note = ""
    pass  # placeholder for Q1: leave this line
    ## ===== Q1: read lines until a blank line. Uncomment ONE option =====

    ## --- Option A ---
    # line = input()
    # while line != "":
    #     note = note + line
    #     line = input()


    ## --- Option B ---
    # line = input()
    # while line != "":
    #     note = note + line + "\n"
    #     line = input()


    ## --- Option C ---
    # line = input()
    # while line != "":
    #     line = input()
    #     note = note + line + "\n"


    ## --- Option D ---
    # line = input()
    # while line != "":
    #     line = input()
    #     note = note + line
    ## ===== end of Q1 =====
    return note


def clean_text(note):
    cleaned = ""
    for ch in note:
        pass  # placeholder for Q2: leave this line
        ## ===== Q2: clean one character. Uncomment ONE option =====

        ## --- Option A ---
        # if ch.isalpha() and ch.isdigit():
        #     cleaned = cleaned + ch
        # else:
        #     cleaned = cleaned + " "


        ## --- Option B ---
        # if ch.isalpha() or ch.isdigit():
        #     cleaned = cleaned + ch
        # else:
        #     cleaned = cleaned + ""


        ## --- Option C ---
        # if ch.isalpha() and ch.isdigit():
        #     cleaned = cleaned + ch.lower()
        # else:
        #     cleaned = cleaned + ""


        ## --- Option D ---
        # if ch.isalpha() or ch.isdigit():
        #     cleaned = cleaned + ch.lower()
        # else:
        #     cleaned = cleaned + " "
        ## ===== end of Q2 =====
    return cleaned


def get_words(cleaned):
    words = []
    pass  # placeholder for Q3: leave this line
    ## ===== Q3: split into words, keep 2+ characters. Uncomment ONE option =====

    ## --- Option A ---
    # for word in cleaned.split():
    #     if len(word) >= 2:
    #         words.append(word)


    ## --- Option B ---
    # for word in cleaned:
    #     if len(word) >= 2:
    #         words.append(word)


    ## --- Option C ---
    # for word in cleaned.split():
    #     if len(word) > 2:
    #         words.append(word)


    ## --- Option D ---
    # for word in cleaned:
    #     if len(word) > 2:
    #         words.append(word)
    ## ===== end of Q3 =====
    return words


def is_palindrome(word):
    left = 0  # placeholder for Q4: leave this line
    right = 0  # placeholder for Q4: leave this line
    ## ===== Q4: where left and right start. Uncomment ONE option =====

    ## --- Option A ---
    # left = 1
    # right = -1


    ## --- Option B ---
    # left = 0
    # right = -1


    ## --- Option C ---
    # left = 0
    # right = len(word) - 1


    ## --- Option D ---
    # left = 1
    # right = len(word) - 1
    ## ===== end of Q4 =====
    while left < right:
        pass  # placeholder for Q5: leave this line
        ## ===== Q5: compare the pair at left and right. Uncomment ONE option =====

        ## --- Option A ---
        # if word[left] == word[right]:
        #     return True


        ## --- Option B ---
        # if word[left] != word[right]:
        #     return False


        ## --- Option C ---
        # if word[left] != word[right]:
        #     return False
        # else:
        #     return True


        ## --- Option D ---
        # if word[left] != word[right]:
        #     break
        ## ===== end of Q5 =====
        left = left + 1
        right = right - 1
    pass  # placeholder for Q6: leave this line
    ## ===== Q6: the line after the loop. Uncomment ONE option =====

    ## --- Option A ---
    # return False


    ## --- Option B ---
    # return left == right


    ## --- Option C ---
    # print(True)


    ## --- Option D ---
    # return True
    ## ===== end of Q6 =====


def unique_palindromes(words):
    found = []
    for word in words:
        pass  # placeholder for Q7: leave this line
        ## ===== Q7: keep each palindrome once. Uncomment ONE option =====

        ## --- Option A ---
        # if is_palindrome(word) and word not in found:
        #     found.append(word)


        ## --- Option B ---
        # if is_palindrome(word) or word in found:
        #     found.append(word)


        ## --- Option C ---
        # if is_palindrome(word) and word in found:
        #     found.append(word)


        ## --- Option D ---
        # if is_palindrome(word) or word not in found:
        #     found.append(word)
        ## ===== end of Q7 =====
    return found


def is_palindrome_rec(word, left, right):
    # BONUS (20 marks, all or nothing). Write this function yourself, without any AI.
    # Rules (the full list is in README.md, "Bonus"):
    # - Keep this first line exactly as it is. It is tested only as
    #   is_palindrome_rec(word, 0, len(word) - 1), including the empty word.
    # - Return True if word[left] to word[right] reads the same both ways.
    # - Each call compares at most ONE pair, word[left] and word[right],
    #   and then calls is_palindrome_rec(word, left + 1, right - 1).
    #   Stop at the first pair that does not match.
    # - Not allowed in this function: for or while loops, slicing (word[1:]),
    #   reversed(), comparing the whole word at once, calling any function
    #   except is_palindrome_rec and len, global, default values, helpers.
    # - Change nothing else in this file for the bonus.
    # - To test it, put a test line such as
    #       print(is_palindrome_rec("level", 0, 4))
    #   just above the line  main()  at the bottom, run the file, then delete
    #   the test line before you submit. A test line left in costs the bonus.
    return False  # placeholder: replace this line with your code


def main():
    print("Type your note. Press Enter on an empty line to finish.")
    note = read_note()
    cleaned = clean_text(note)
    words = get_words(cleaned)
    palindromes = unique_palindromes(words)
    pass  # placeholder for Q8: leave this line
    ## ===== Q8: print the result. Uncomment ONE option =====

    ## --- Option A ---
    # if palindromes == "":
    #     print("(none)")
    # else:
    #     print(", ".join(palindromes))


    ## --- Option B ---
    # if len(palindromes) == 0:
    #     print("(none)")
    # else:
    #     print(palindromes)


    ## --- Option C ---
    # if len(palindromes) == 0:
    #     print("(none)")
    # else:
    #     print(", ".join(palindromes))


    ## --- Option D ---
    # if palindromes == "":
    #     print("(none)")
    # else:
    #     print(palindromes)
    ## ===== end of Q8 =====


main()
