import re
import string
from collections import Counter
import numpy as np

def read_file(filename):
  with open(filename, encoding="utf8") as file:
    lines = file.readlines()
    words = []
    for line in lines:
      words += re.findall(r'\w+', line.lower())

  return words
words=read_file("./the-adventures-of-huckleberry-finn.txt")
a=set(words)
counts = Counter(words)


