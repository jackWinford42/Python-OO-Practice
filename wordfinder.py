"""Word Finder: finds random words from a dictionary."""
from random import randrange
class WordFinder:
    def create_list(self):
        """Create a list of random words from a source file"""
        file1 = open(self.p, 'r')
        self.l = file1.readlines()

        for line in self.l:
            #print(format(line.rstrip()))
            self.l[self.l.index(line)] = format(line.rstrip())

    def __init__(self, path):
        """Create the word finder for a certain file path"""
        self.p = path
        self.l = []
        self.create_list()
        print(f"{len(self.l)} words read")

    def random(self):
        """Return a random word from the list of random words"""
        return self.l[randrange(len(self.l))]

class SpecialWordFinder(WordFinder):
    def create_list(self):
        """Create a special list of random words from a source file"""
        file1 = open(self.p, 'r')
        self.l = file1.readlines()
        print(self.l)
        for line in self.l:
            #Not sure what is wrong here but some of the returned lines are not deleted
            #such as /n lines or blank lines but some are.
            #Also the solution is not helpful because Springboard implemented this in
            #a very different way from me and I don't want to just copy their solution.
            if line == "\n" or line[0] == "#":
                self.l.remove(line)
            else:
                self.l[self.l.index(line)] = format(line.rstrip())
        print(self.l)
