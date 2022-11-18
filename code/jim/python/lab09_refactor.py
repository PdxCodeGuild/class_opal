"""
Calculatation of ARI score for a given text in .txt file.
The .txt file should be located in a 'data' folder inside the directory containing this .py file. 
Note that this code uses pathlib library. See:
https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
"""

from math import ceil
from pathlib import Path
import re

ARI_SCALE = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


def count_sentences(contents: str):
    """Counts the number of sentences in string."""
    if any(x in contents for x in ['.','?','!']):
        return len(re.split(r'[.!?][ ]', contents))
    else:
        return 0


def calculate_ari(characters: float, words: float, sentences: float):
    """Calculates ARI score, rounded up, based on a string of text."""
    if words == 0 or sentences == 0:
        return 1
    else:
        return max(min(ceil(4.71 * characters / words + 0.5 * words / sentences - 21.43), 14),1)


if __name__ == '__main__':
    filename = Path("data/frankenstein.txt")
    contents = filename.read_text(encoding="utf8")

    characters = len(contents)
    words = len(contents.split())

    sentences = count_sentences(contents)

    ari_score = calculate_ari(characters, words, sentences)

    print(f"""
--------------------------------------------------------

The ARI for {filename.name} is {ari_score}.
This corresponds to a {ARI_SCALE[ari_score]['grade_level']} level of difficulty
that is suitable for an average person {ARI_SCALE[ari_score]['ages']} years old.

--------------------------------------------------------
""")