import preprocess
import csv
file=open('Data.csv')
reader=csv.reader(file)
data=list(reader)
file.close()
file=open("Words.txt")
words=[line.rstrip('\n') for line in file]
file.close()
def anagram(string):
	record=preprocess.generate_entry(string)
	indices=set()
	anagrams=[]
	for i in range(0,26):
		if(record[i]!=0):
			indices.add(i)
	print(indices)
	for i in range(0,len(data)) :
		f=0
		word=data[i]
		if int(word[26]) == record[26]:
			f=1
			for j in indices:
				if(int(word[j])!=record[j]):
					f=0
					break
		if(f==1):
			anagrams.append(i)
	print(str(len(anagrams)) + " Words found ")
	for i in anagrams:
		print(words[i])

def build(string):
	record = preprocess.generate_entry(string)
	indices = set()
	builds = []
	for i in range(0, 26):
		if (record[i] != 0):
			indices.add(i)
	print(indices)
	for i in range(0, len(data)):
		f = 0
		word = data[i]
		if int(word[26]) <= record[26]:		#checks length of word
			f = 1
			margin=record[26]-int(word[26])		#diff between two lengths
			error=0
			for j in indices:
				if (int(word[j]) > record[j]):		#can't have more characters in the checked word
					f = 0
					break
				else:
					error=error+record[j]-int(word[j])
			if(error!=margin):
				f=0
		if (f == 1):
			builds.append(i)
	print(str(len(builds)) + " Words found ")
	for i in builds:
		print(words[i])



