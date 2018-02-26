from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
    	for word in WORD_RE.findall(line):
    		yield ("", word)

    def reducer(self, key, values):
    	k = 0
    	for i in values:
    		if(len(i)==3):
    			k=k+1
    	yield ("three letter words", k)


if __name__ == '__main__':
    MRWordFrequencyCount.run()