import time
from collections import Counter
from collections import defaultdict


# normal data structures speed
# set enhancing iteration and other examples


# anagramy


def timeit(func):

    def decorating(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print("Execution time: {}".format(stop - start))
        return result
    return decorating


@timeit
def is_anagram(first, second):
    first = sorted(first)
    second = sorted(second)
    return first == second


@timeit
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


@timeit
def is_anagram_counter(first, second):
    return Counter(first) == Counter(second)


# assert is_anagram("ooo", "bbb") == False
# assert is_anagram("python", "thonpy") == True

# assert is_anagram_counter("ooo", "bbb") == False
# assert is_anagram_counter("ooo", "ooob") == False
# assert is_anagram_counter("oooc", "ooob") == False
# assert is_anagram_counter("python", "thonpy") == True


# assert is_anagram_defaultdict("ooo", "bbb") == False
# assert is_anagram_defaultdict("ooo", "ooob") == False
# assert is_anagram_defaultdict("oobb", "ooob") == False
# assert is_anagram_defaultdict("abbbbc", "abbbcc") == False
# assert is_anagram_defaultdict("python", "thonpy") == True


with open('anagram1.txt') as fd:
    word1 = "".join([line.strip() for line in fd])

with open('anagram2.txt') as fd:
    word2 = "".join([line.strip() for line in fd])


print is_anagram(word1, word2)
print is_anagram_counter(word1, word2)
print is_anagram_defaultdict(word1, word2)
# wniosek: porownywanie counterow nie jest najszybsze


# how many pairs are equal to threshold


def pairs(numbers, threshold):
    cnts = Counter(numbers)
    res = 0
    for numb in cnts:
        item_cnt, pair_cnt = cnts[numb], cnts[threshold - numb]
        if pair_cnt:
            if 2 * numb == threshold:
                res += item_cnt * (item_cnt - 1)
            else:
                res += item_cnt * pair_cnt
    return res / 2


assert pairs([1, 2, 10, 11, 3, 3, 3, 4], 6) == 4


# Counter - count distance

text1 = "oh my god this is not good"
text2 = "oh your god this is not good"

print Counter(text1.split(" "))
print Counter(text2.split(" "))
print Counter(text1.split(" ")) - Counter(text2.split(" "))

message1 = "pplrec"
message2 = "ppl2rec"
print Counter(message1) - Counter(message2)


# namedtuple - speedup for simple classes -> separate file


# deque - queue with limit


