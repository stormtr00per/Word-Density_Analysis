from Parse import *
from Process import *
import sys

class main:
	try:
		if len(sys.argv) < 2:
			url = raw_input("Please enter URL: ")
			if ' ' in url:
				raise Exception("InputError")
			parseObj = Parse(url)
		else:
			url = sys.argv[1]
			parseObj = Parse(url)
	except ValueError as e :
		print(e)
		sys.exit()

	title = parseObj.getTitle()
	keyword = parseObj.getKeyword()

	content = parseObj.getParsedContent()
	content = content[-20:]

	header = parseObj.getParsedHeader(title, keyword)
	header = header[-10:]

	analyzer = mergeBag(header, content, 3)
	analyzer = sortBag(analyzer)
	analyzer = list(analyzer[-8:])
	analyzer.reverse()

	print("\nWebpage: " + url)
	print('\nKeywords:')
	for w in analyzer:
		print(w[0])
	print('')
