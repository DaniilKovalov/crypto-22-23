# 2.txt - __ text
# 3.txt - no space
import re
import math
from collections import Counter


def find_monogram(text):
    big_lst = re.findall(r'\w', text)
    clear_lst = set(big_lst)
    letters = {}
    counter = 0
    for letter in clear_lst:
        letters[letter] = len(re.findall(letter, text))
        counter += len(re.findall(letter, text))
    for i in letters:
        letters[i] = float(letters[i]/counter)
    return letters


def find_bigram(text, counter):
    big_lst = re.findall(r'\w\w', text)
    clear_lst = set(big_lst)
    bigrams = {}
    for i in clear_lst:
        bigrams[i] = len(re.findall(i, text))
        counter += len(re.findall(i, text))
    return bigrams, counter


def cross_bigrams(text):
    all_bigr, counter = find_bigram(text, 0)
    res = {}
    for i in all_bigr:
        res[i] = float(all_bigr[i] / counter)
    return res


def no_cross_bigrams(text):
    txt_lst = list(text)
    res = []
    i = 0
    while i < len(txt_lst) - 1:
        res.append(txt_lst[i] + txt_lst[i + 1])
        i += 2
    res = Counter(res)
    counter = 0
    for i in res.values():
        counter += i
    for i in res:
        res[i] = float(res[i]/counter)
    return res


def find_entropy(frequency, nrgams):
    entropy = 0
    for values in frequency.values():
        entropy += - values * math.log(values, 2)
    entropy *= 1 / nrgams
    return entropy


def find_r(entrop, elements):
    r = 1 - (entrop/math.log2(elements))
    return r


def sort_dict(dct):
    sorted_dict = {}
    sorted_keys = sorted(dct, key=dct.get)
    for w in reversed(sorted_keys):
        sorted_dict[w] = dct[w]
    return sorted_dict


def print_ngrams(dct):
    column = sort_dict(dct)
    count = 0
    for row in list(column.keys())[:10]:
        print(f"{row} --- {to_fixed(column[row], 10)}")
        count += column[row]


def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"


space_txt = open('2.txt', 'r').read()
no_space_txt = open('3.txt', 'r').read()
num_of_letters = 33
num_of_letters_no_space = 34

space_monograms = find_monogram(space_txt)  # монограммы
space_monograms_entropy = find_entropy(space_monograms, 1)
space_monograms_r = find_r(space_monograms_entropy, num_of_letters_no_space)
no_space_monograms = find_monogram(no_space_txt)
no_space_monograms_entropy = find_entropy(no_space_monograms, 1)
no_space_monograms_r = find_r(no_space_monograms_entropy, num_of_letters)

space_bigrams = no_cross_bigrams(space_txt)  # биграммы
space_bigrams_entropy = find_entropy(space_bigrams, 2)
space_bigrams_r = find_r(space_bigrams_entropy, num_of_letters_no_space)
space_no_cross_bigrams = cross_bigrams(space_txt)
space_no_cross_bigrams_entropy = find_entropy(space_no_cross_bigrams, 2)
space_no_cross_bigrams_r = find_r(space_no_cross_bigrams_entropy, num_of_letters_no_space)
no_space_bigrams = no_cross_bigrams(no_space_txt)
no_space_bigrams_entropy = find_entropy(no_space_bigrams, 2)
no_space_bigrams_r = find_r(no_space_bigrams_entropy, num_of_letters)
no_cross_no_space_bigrams = cross_bigrams(no_space_txt)
no_cross_no_space_bigrams_entropy = find_entropy(no_cross_no_space_bigrams, 2)
no_cross_no_space_bigrams_r = find_r(no_cross_no_space_bigrams_entropy, num_of_letters)

print(f"h1 in text with space {space_monograms_entropy}")
print(f"r1 in text with space {space_monograms_r}")
print(f"h1 in text without space {no_space_monograms_entropy}")
print(f"r1 in text without space {no_space_monograms_r}\n")

print(f"h2 in text with space {space_bigrams_entropy}")
print(f"r2 in text with space {space_bigrams_r}")
print(f"no cross h2 in text with space {space_no_cross_bigrams_entropy}")
print(f"no cross r2 in text with space {space_no_cross_bigrams_r}")
print(f"h2 in text without space {no_space_bigrams_entropy}")
print(f"r2 in text without space {no_space_bigrams_r}")
print(f"no cross h2 in text without space {no_cross_no_space_bigrams_entropy}")
print(f"no cross r2 in text without space {no_cross_no_space_bigrams_r}")

print_ngrams(space_bigrams)
print('----------')
print_ngrams(space_no_cross_bigrams)
print('----------')
print_ngrams(no_space_bigrams)
print('----------')
print_ngrams(no_cross_no_space_bigrams)
# print_ngrams(no_space_bigrams)
# print_ngrams(no_cross_bigrams(space_txt))
