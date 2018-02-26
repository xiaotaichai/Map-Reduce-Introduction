from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
    	for word in WORD_RE.findall(line):
    		yield ("", word.lower())

    def reducer(self, key, values):
    	k = 0
    	for i in values:
    		if(i == "the" or i == "The"):
    			k=k+1
    	yield ("the", k)


if __name__ == '__main__':
    MRWordFrequencyCount.run()


# from mrjob.job import MRJob

# class MRWordFrequencyCount(MRJob):

#     def mapper(self, _, line):
#     	words = line.split()
#     	yield ("", words)

#     def reducer(self, key, values):
#     	#word = input("the")
#     	k = 0
#     	for i in values:
#     		if(i=='the'):
#     			k=k+1
#     	yield (key, k)


# if __name__ == '__main__':
#     MRWordFrequencyCount.run()

