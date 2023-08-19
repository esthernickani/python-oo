"""Word Finder: finds random words from a dictionary."""

import random 
class WordFinder:

    def __init__(self, file_path):
        self.file_path = file_path
        self.word_list = []
        self.read_file()
    
    def read_file(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.word_list.append(line.rstrip('\n'))
            print(len(self.word_list))
    
    def random(self):
        return random.choice(self.word_list)

class SpecialWordFinder(WordFinder):
    def read_file(self):
        super().read_file()
        self.word_list = [word for word in self.word_list if word and not word.startswith('#')]
    ...
