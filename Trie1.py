from typing import Tuple
import re
import string
from collections import Counter
import numpy as np


class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):

        for key in keys:
            self.insert(key)  # inserting one key to the trie.

    def insert(self, key):

        node = self.root

        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def search(self, key):
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]

        return node and node.last and found

    def suggestionsRec(self, node, word):
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)

        for i in range(0,10):
            print(self.word_list[i])
        return 1
with open("the-adventures-of-huckleberry-finn.txt", encoding="utf8") as file:
    lines = file.readlines()
    words = []
    for line in lines:
        words += re.findall(r'\w+', line.lower())
keys=words

key = input().lower()
status = ["Not found", "Found"]


t = Trie()

t.formTrie(keys)

comp = t.printAutoSuggestions(key)

if comp == -1:
    print("No other strings found with this prefix\n")
elif comp == 0:
    print("No string found with this prefix\n")

