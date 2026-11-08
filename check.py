"""Check the STRUCTURE of palindromes.py before you submit.

Run:  python3 check.py

It checks that Python can read the file, and that each gap Q1 to Q8 has
exactly ONE option uncommented. It does NOT run your program and does NOT
tell you if any choice is right.
"""

import ast
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(HERE, "palindromes.py")
GAPS = ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"]


def read_gaps(lines):
    """Return {gap: {letter: [active, commented]}} and a list of stray active lines."""
    gaps = {}
    stray = []
    gap = None
    letter = None
    for number, line in enumerate(lines, start=1):
        s = line.strip()
        start = re.match(r"#+ ?===== (Q\d):", s)
        option = re.match(r"#+ ?--- Option ([A-D]) ---", s)
        if start:
            gap = start.group(1)
            letter = None
            gaps[gap] = {}
        elif re.match(r"#+ ?===== end of", s):
            gap = None
        elif gap and option:
            letter = option.group(1)
            gaps[gap][letter] = [0, 0]
        elif gap and s:
            if letter is None:
                if not s.startswith("#"):
                    stray.append(f"{gap}, line {number}")
            elif s.startswith("#"):
                gaps[gap][letter][1] += 1
            else:
                gaps[gap][letter][0] += 1
    return gaps, stray


def main():
    if not os.path.exists(FILE):
        print("palindromes.py is missing.")
        return
    text = open(FILE, encoding="utf-8").read()
    ok = True
    try:
        ast.parse(text)
    except SyntaxError as error:
        print(f"Python cannot read palindromes.py: line {error.lineno}: {error.msg}")
        print("  Often this means an option is only partly uncommented, or its indentation changed.")
        ok = False

    gaps, stray = read_gaps(text.splitlines())
    for g in GAPS:
        if g not in gaps:
            print(f"{g}: its block is missing. Did a '## =====' line get deleted?")
            ok = False
            continue
        active = [l for l, (a, c) in gaps[g].items() if a > 0]
        partly = [l for l, (a, c) in gaps[g].items() if a > 0 and c > 0]
        if len(active) == 0:
            print(f"{g}: no option chosen yet.")
            ok = False
        elif len(active) > 1:
            print(f"{g}: {len(active)} options are uncommented ({', '.join(active)}). Keep only one.")
            ok = False
        for l in partly:
            print(f"{g}: option {l} is only partly uncommented. Uncomment all of its lines.")
            ok = False
    for s in stray:
        print(f"Code outside an option in {s}. Put it back as it was.")
        ok = False

    if ok:
        print("palindromes.py: Python can read it, and every gap has exactly one option.")
        print("This does not check if your choices are right. Submit palindromes.py on Ed.")


if __name__ == "__main__":
    main()
