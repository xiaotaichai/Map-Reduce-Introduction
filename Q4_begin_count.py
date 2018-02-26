from mrjob.job import MRJob
from pandas import Series
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            s = [word[0].lower()]
        yield (s, len(word))

    def reducer(self, key, values):
    	yield (key, sum(values))


if __name__ == '__main__':
    MRWordFrequencyCount.run()