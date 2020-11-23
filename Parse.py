import urllib3
from bs4 import BeautifulSoup
from Process import *


class Parse:
	def __init__(self, url=None):
		try:
			http = urllib3.PoolManager()
			page = http.request('GET', url)
			content = page.data.decode('utf-8')
			soup = BeautifulSoup(content, "html.parser")
			soup.encode('utf-8')
			[s.replaceWith(" ") for s in soup('link', 'article', 'style',
			'script', 'head')]
		except:
			raise ValueError('Unable to get content from '+url)

		invalid_tags = ['b', 'i', 'u', 'strong', 'a']
		for tag in invalid_tags:
			for match in soup.findAll(tag):
				match.replaceWithChildren()

		self.soup = soup;
		pass;


	def getTitle(self):
		return self.soup.title.get_text()


	def getKeyword(self):
		tag = self.soup.find("meta", {"name":"keywords"})
		if(tag== None):
			return "";
		else:
			return parseText(tag['content']);


	def getHeaders(self):
		headingText = []
		for i in range(1,4):
			heading = self.soup.find('h'+str(i))
			if heading != None:
				headingText.append(parseText(heading.get_text()))
		return headingText


	def getContent(self):
		ans=[]
		str = ""
		self.getContentRes(None,ans)
		for txt in ans:
			str+= txt+" "
		return parseText(str)


	def getContentRes(self,node,ans):
		if(node == None):
			node = self.soup

		if(len(str(node)) == 0):
			return
		ratio = len(node.get_text())/float(len(str(node)))
		if(ratio > 0.8):
			ans.append(parseText(node.get_text())+" ")
		else:
			for i in range(len(node.findChildren(recursive = False))):
				self.getContentRes(node.findChildren(recursive = False)[i],ans)


	def getParsedContent(self):
		content = self.getContent()
		content = unigram(content)
		content = removeStopWord(content)
		content = sortBag(content)
		return content


	def getParsedHeader(self, title, keyword):
		head = self.getHeaders()
		header = title + " " + keyword
		for tag in head:
			header += " " + tag
		header = unigram(header)
		header = removeStopWord(header)
		header = sortBag(header)
		return header
