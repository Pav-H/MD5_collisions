# -*- coding: utf8 -*-
import itertools
import hashlib
import unicodedata as ucd
import sys


# UTF-8 symbols generator
def dumpEncoding(enc):
    arr = []
    for i in range(sys.maxunicode):
        u = chr(i)
        try:
            s = u.encode(enc)
        except UnicodeEncodeError:
            continue
        try:
            name = ucd.name(u)
        except:
            name = '?'
            arr.append(s)
    return arr


# tuple to string
def tupToStr(tup: tuple):
    flatten = [str(item) for sub in tup for item in sub]
    s = "".join(flatten)
    return s


def getLastNbait(s: str, n: int):
    s_new = ""
    for i in range(1, n*2 + 1):
        s_new += s[-i]
    return s_new


if __name__ == "__main__":
    my_string = "Hello World"
    my_hashed_string = hashlib.md5(my_string.encode("UTF-8")).hexdigest()
    print(f"Hello World = {my_hashed_string}")
    n = input("Choose n ( 0 < n < 16) baits to broot hash: ")
    char_str = dumpEncoding("UTF-8")
    for i in range(1, len(my_string)):
        for c in itertools.combinations_with_replacement(char_str, i):
            comb = tupToStr(c)
            hashed_comb = hashlib.md5(comb.encode("UTF-8")).hexdigest()
            if getLastNbait(hashed_comb, int(n)) == getLastNbait(my_hashed_string, int(n)):
                print(f"Found collision: {comb} = {hashed_comb}")
