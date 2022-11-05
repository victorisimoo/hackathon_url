# author: victorisimo
# description: hackaton
from typing import List

def justify_method(words, max_lenght):
    lines = []
    curr = []
    width = 0
    i = 0

    while i < len(words):
        word = words[i]
        new_width = width + len(word) + bool(curr)
        if new_width <= max_lenght:
            i += 1
            curr.append(word)
            width = new_width
        elif curr:
            lines.append(add_spaces(curr, max_lenght, format_text=True))
            curr = []
            width = 0
    if curr:
        lines.append(add_spaces(curr, max_lenght, format_text=False))
    return lines


def add_spaces(words, max_size, format_text):
    if format_text:
        wid, remainder = divmod(max_size - sum(len(w) for w in words), len(words) - 1)
        text_wi = [wid + int(i < remainder) for i in range(len(words) - 1)]
        text_wi.append(0)
    else:
        text_wi = [1 for _ in range(len(words) - 1)]
        text_wi.append(max_size - sum(len(w) for w in words) - len(words) - 1)

    return ''.join(
        w + (' ' * wid)
        for w, wid in zip(words, text_wi)
    )

# main methodxw
if __name__ == '__main__':
    print(justify_method(['This is an', 'example of text', 'justification.'], 26))