import re
import string
from collections import Counter
import numpy as np
class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True
        # node.counter += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def suggestionsRec(self, node, word):

        # Method to recursively traverse the trie
        # and return a whole word.
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):

        # Returns all the words in the trie whose common
        # prefix is the given key thus listing out all
        # the suggestions for autocomplete.
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

        for s in self.word_list:
            print(s)
        return 1
