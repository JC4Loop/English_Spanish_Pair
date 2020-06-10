from pairDb import*
from PairInput import *
from Word import *
from NonEngConversion import*
#from xml.etree.ElementTree import Element, SubElement, tostring
import xml.etree.ElementTree as ET

data = getPairs()
root = ET.Element('EspEngData')

i = 0

datanew = []

espWord = ""
engWord = ""

for d in data:
	if i % 2 == 0:
		espWord = d.word #espWord = replaceWithLatin1Char(row[1])
		i += 1
		continue
	else:
		engWord = d.word
		datanew.append(PairInput(espWord,engWord))
	i += 1



for d in datanew:
	word = ET.SubElement(root, "word")

	spanish = ET.SubElement(word, "spanish")
	english = ET.SubElement(word, "english")
	spanish.text = d.espW
	english.text = d.engW

#print(ET.tostring(root))

# Output XML to xml file - same directory
#tree = ET.ElementTree(root)
#tree.write('pairData.xml')


xml = (bytes('<?xml version="1.0" encoding="UTF-8"?><?xml-stylesheet type="text/xsl" href="pairsDataStyle.xsl"?>', encoding='utf-8') + ET.tostring(root))
xml = xml.decode('utf-8')
with open('pairData.xml', 'w+') as f:
    f.write(xml)
    print('Written XML')