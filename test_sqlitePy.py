import sqlite3
import PairClasses as pc
from NonEngConversion import*

def getConnection():
	return sqlite3.connect('EspEng.db')


def getPairs():
	pairsToReturn = []
	c = getConnection()
	cur = c.cursor()
	cur.execute("SELECT english.word, spanish.word FROM english INNER JOIN pairtable ON english.id = pairtable.engId INNER JOIN spanish ON pairtable.espId = spanish.id")
	rows = cur.fetchall()
	integer = 1
	for row in rows:
		print(row[0],"\t",row[1])
		espWord = replaceWithLatin1Char(row[1])
		esp = pc.Word(espWord,integer,"esp")
		eng = pc.Word(row[0],integer,"eng")
		pairsToReturn.append(pc.Pair(esp,eng))
		integer += 1
	c.close()
	return pairsToReturn



'''
conn = getConnection()
c = conn.cursor()

c.execute("SELECT english.word, spanish.word FROM english INNER JOIN pairtable ON english.id = pairtable.engId INNER JOIN spanish ON pairtable.espId = spanish.id")
#FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id 

rows = c.fetchall()

for row in rows:
		#print("ID = \t", row[0], end = '') # print without new line
		print(row[0],"\t",row[1])

conn.close()
'''

data = getPairs()
print("Length of pairs =",len(data))