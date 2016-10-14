from lxml import etree
import os, codecs
from pymystem3 import Mystem

def getAnalyzedTexts(file_):
	analyzes = []
	f = '<xml>%s</xml>'%codecs.open(file_, 'r', 'utf8').read()
	parser = etree.XMLParser()
	tree = etree.XML(f, parser)
	texts = [i.text for i in tree.findall('.//text')]
	m = Mystem()
	for i in texts:
		try:
			s = m.analyze(i)
			analyzes.append(s)
			# print(s)
		except:
			pass
	return analyzes

if __name__ == '__main__':
	analyzes = []
	ls = os.listdir(os.getcwd())
	for i in ls:
		if os.path.splitext(i)[-1] == '.txt':
			analyzes += getAnalyzedTexts(i)
	fres = codecs.open('fres.txt', 'w', 'utf8')
	for i in analyzes:
		fres.write(repr(i))
	fres.close()
	f = codecs.open('fres.txt', 'r', 'utf8').read().split('}, {')
	fres = codecs.open('fres2.txt','w','utf8')
	for i in f:
		fres.write('{%s}\r\n'%i)
	fres.close()

