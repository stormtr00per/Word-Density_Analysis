from Parse import *
import re


file = 'stopword.txt'

def parseText(content):
	text = content.encode('utf-8','ignore')
	text = text.lower()
	text = re.sub(r'([^\s\w]|_|\n|\t|\r)+', ' ', text)
	text = re.sub(' +',' ',text)
	return text

def unigram(content):
	counts = {}
	words = content.split(" ");
	for word in words:
		if( word in counts ):
			counts[word]+=1
		else:
			counts[word]=1

	arr = []
	for c in counts:
		arr.append((c,counts[c]))
	return arr

def getStopWord():
	words=[]
	with open(file) as f:
		for line in f.readlines():
			words.append(line.strip('\n'))
	return words

def removeStopWord(bag):
	stopwords = getStopWord()
	newbag = []
	for b in bag:
		if(b[0] not in stopwords):
			newbag.append(b)
	return newbag

def sortBag(bag):
	return sorted(bag, key=lambda b: b[1])

def mergeBag(header,content,weight=1):
	counts = {}
	ans = []
	for b in header:
		counts[b[0]] = b[1]*weight
	for b in content:
		if(b[0] in counts):
			counts[b[0]]+=b[1]
		else:
			counts[b[0]]=b[1]
	for k in counts:
		ans.append((k,counts[k]))
	return ans
