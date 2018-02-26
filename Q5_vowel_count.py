from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            s = [len(word)]
        yield (s, word.lower())

    def reducer(self, key, values):
    	for word in values:
    		numVowels = sum(x in 'aeiou' for x in word)
    	yield (key, numVowels)


if __name__ == '__main__':
    MRWordFrequencyCount.run()