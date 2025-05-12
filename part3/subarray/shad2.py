"""
ээээ тоже на тему камсам и префиксов


Условие: строка симметричная, если exist i: set(s[:i]) == set(s[i:]). Надо сказать, является ли строка симметричной

мне понравилась идея представить каждую букву как вектор и камсам по строке сделать из таких векторов
"""

str_line = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"


def append_dicts(a, b):
    c = {ch: a[ch] + b[ch] for ch in alphabet}
    return c


def diff_dicts(a, b):
    c = {ch: a[ch] - b[ch] for ch in alphabet}
    return c


def is_equal(a, b):
    c = {ch: bool(cnt) for ch, cnt in a.items()}
    d = {ch: bool(cnt) for ch, cnt in b.items()}
    return c == d


all_chars = {ch: 0 for ch in alphabet}

for i in range(len(str_line)):
    ch = str_line[i]
    all_chars[ch] += 1

current_part = {ch: 0 for ch in alphabet}

good = False
for i in range(len(str_line) // 2):
    current_part[str_line[i]] += 1

    if is_equal(
        current_part,
        diff_dicts(all_chars, current_part),
    ):
        good = True
        break

if good:
    print("YES")
else:
    print("NO")


# был еще варик задачки где строка состоит только из 0-9 и тогда решение выглядит красивее

import numpy as np

num_string = input()

all_nums_count = np.bincount([int(num) for num in num_string], minlength=10)

nums_count = np.zeros(10)
yes = False
for num in num_string:
    nums_count[int(num)] += 1

    if not (nums_count.astype(bool) ^ (all_nums_count - nums_count).astype(bool)).any():
        yes = True
        print("YES")
        break

if not yes:
    print("NO")
