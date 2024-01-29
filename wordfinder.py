"""Word Finder: finds random words from a dictionary.

>>> wf = WordFinder("/Users/student/words.txt")
3 words read

>>> wf.random()
'cat'

>>> wf.random()
'cat'

>>> wf.random()
'porcupine'

>>> wf.random()
'dog'
"""

import random

class WordFinder:

    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)
        print(f"There are {len(self.words)} words")

    def parse(self, file):
        return [w.strip() for w in file]

    def random(self):
        return random.choice(self.words)
    
