from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        words = WORD_RE.findall(line)
        for word in words:
            s = [word[0].lower()]
        yield (s, len(words))

    def reducer(self, key, values):
    	yield (key, sum(values))


if __name__ == '__main__':
    MRWordFrequencyCount.run()