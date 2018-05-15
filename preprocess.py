alphabets="QWERTYUIOPASDFGHJKLZXCVBNM."  #. is for the length of str
"""
Generate dict
read txt file
for each word, generate a new dict
update csv file

"""
def generate_entry(string):
	entry={}
	for buff in alphabets:
		entry[buff]=0
	for char in string:
		try:
			entry[char]=entry[char]+1
		except:
			print("Wild Card detected")
	entry['.']=len(string)
	record=[]
	for char in alphabets:
		record.append(entry[char])
	return (record)

def enter_record(record):
	import csv
	file=open("Data.csv",'a',newline='')
	writer = csv.writer(file)
	writer.writerow(record)

def main():
	file=open("Words.txt","r")
	contents = [line.rstrip('\n') for line in file]
	for word in contents:
		if(word!="\n"):

			print(word)
			enter_record(generate_entry(word))

#main()

