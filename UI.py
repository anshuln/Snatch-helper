import Algos
while True:
	word=input("Enter a word \n")
	word=word.upper()
	choice=input("Enter 1 for anagrams, 2 for build , 3 for pattern \n")
	if choice == '1':
		Algos.anagram(word)
	elif choice == '2':
		Algos.build(word)
	elif choice == '3':
		Algos.pattern(word)
	else:
		break
