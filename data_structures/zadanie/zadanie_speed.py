import timeit
from functools import partial
from collections import defaultdict, Counter


def is_anagram(first, second):
    first = sorted(first)
    second = sorted(second)
    return first == second


def is_anagram_defaultdict(first, second):
    fres = defaultdict(int)
    sres = defaultdict(int)
    for i in first:
        fres[i] += 1
    for j in second:
        sres[j] += 1
    for i in fres:
        if fres[i] != sres[i]:
            return False
    return len(first) == len(second)


def is_anagram_counter(first, second):
    return Counter(first) == Counter(second)



with open('../anagram1.txt') as fd:
    word1 = "".join([line.strip() for line in fd])

with open('../anagram2.txt') as fd:
    word2 = "".join([line.strip() for line in fd])



is_a_dd = partial(is_anagram_defaultdict, word1, word2)
is_a_cnt = partial(is_anagram_counter, word1, word2)
is_a = partial(is_anagram, word1, word2)


time = 0
cnt = 10
for i in range(cnt):
    time += timeit.timeit(is_a_dd, number=100)

print("Is anagram DefaultDict: {}".format(time/float(cnt)))


time = 0
for i in range(cnt):
    time += timeit.timeit(is_a_cnt, number=100)

print("Is anagram Counter: {}".format(time/float(cnt)))


time = 0
for i in range(cnt):
    time += timeit.timeit(is_a, number=100)
print("Is anagram: {}".format(time/float(cnt)))
