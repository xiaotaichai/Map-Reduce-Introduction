from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
    	words = line.split()
    	yield ("", words.lower())

    def combiner(self, key, values):
    	word = input("the")
    	k = 0
    	for i in values:
    		if(i==word):
    			k=k+1
    	yield ("the", k)

    def reducer(self, key, values):
    	yield key, sum(k)


if __name__ == '__main__':
    MRWordFrequencyCount.run()