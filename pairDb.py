import psycopg2
import PairClasses as pc
from NonEngConversion import*

def getConnection():
	conn = psycopg2.connect(database = "engEspDeuDb", user = "justin", password = "password", host = "127.0.0.1", port = "5432")
	return conn

def getPairs():
	pairsToReturn = []
	c = getConnection()
	cur = c.cursor()
	cur.execute("SELECT  pairEngEsp.id, spanish.word, english.word,pairEngEsp.timescorrect,pairEngEsp.timesincorrect FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id ORDER BY timescorrect;")
	rows = cur.fetchall()
	for row in rows:
		#print("ID = \t", row[0], end = '') # print without new line
		espWord = replaceWithLatin1Char(row[1])
		esp = pc.Word(espWord,row[0],"esp")
		eng = pc.Word(row[2],row[0],"eng")
		pairsToReturn.append(pc.Pair(esp,eng))


	c.close()
	return pairsToReturn

def getPairsByLetter(letter):
	letLower = letter.lower()
	#print("letter is ",letter)
	pairsToReturn = []
	c = getConnection()
	cur = c.cursor()
	selquery = "SELECT  pairEngEsp.id, spanish.word, english.word,pairEngEsp.timescorrect,pairEngEsp.timesincorrect FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id WHERE lower(spanish.word) SIMILAR TO (%s) OR upper(spanish.word) SIMILAR TO (%s) ORDER BY timescorrect"
			   #SELECT  pairEngEsp.id, spanish.word, english.word,pairEngEsp.timescorrect,pairEngEsp.timesincorrect FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id WHERE lower(spanish.word) SIMILAR TO 'l%' ORDER BY timescorrect;


	letLower = letLower + "%"
	letter = letter + "%"
	#args = "(" + letLower + "|" + letter + ")%"
	#args = "(" + letter + "|" + letLower + ")%"
	cur.execute(selquery,(letLower,letter))
	rows = cur.fetchall()
	for row in rows:
		#print("\tSpanish Word = ", row[1], end = '')
		#print("\tEnglish Word = ", row[2])
		espWord = replaceWithLatin1Char(row[1])
		esp = pc.Word(espWord,row[0],"esp")
		eng = pc.Word(row[2],row[0],"eng")
		pairsToReturn.append(pc.Pair(esp,eng))

	c.close()
	return pairsToReturn



def incrementTimesCorrect(pairID):
	count = 0
	try:
		c = getConnection()
		cur = c.cursor()

		updateQuery = "UPDATE pairEngEsp SET timescorrect = timescorrect + 1 WHERE id = %s;"
		cur.execute(updateQuery,(pairID,))
		c.commit()
		count = cur.rowcount

	except(Exception,psycopg2.Error) as error:
		print("Error in update",error)

	finally:
		if (c):
			cur.close()
			c.close()
			return count

#when chosen pair is incorrect both pairIDs will be incremented
def incrementTimesInCor(pairID1,pairID2):
	count = 0
	try:
		c = getConnection()
		cur = c.cursor()
		updateQuery = "UPDATE pairEngEsp SET timesincorrect = timesincorrect + 1 WHERE id in  (%s,%s);"
		cur.execute(updateQuery,(pairID1,pairID2))
		c.commit()
		count = cur.rowcount
		#print(count,"Updates successful (incorrect incremented)")

	except(Exception,psycopg2.Error) as error:
		print("Error in incor update",error)

	finally:
		if(c):
			cur.close()
			c.close()
			return count

def handleAllInput(pairsCollection):
	count = 0
	for i in range(0,len(pairsCollection)):
		count += savePairToDb(pairsCollection[i])
	return count

def savePairToDb(pair):
	
	englishWord = pair.getEngW()
	spanishWord = pair.getEspW()
	print(englishWord,spanishWord)
	count = 0
	try:
		c = getConnection()
		cur = c.cursor()
		#insertQuery = "INSERT INTO english (word) SELECT %s WHERE NOT EXISTS (SELECT id FROM english WHERE word = %s) RETURNING id;"
		inOrSelQuery = "WITH S AS (SELECT id FROM english WHERE word = %s), I AS (INSERT INTO english (word) SELECT %s WHERE NOT EXISTS (SELECT id FROM english WHERE word= %s) RETURNING id) SELECT id FROM I UNION ALL SELECT id FROM S;"
		cur.execute(inOrSelQuery,(englishWord,englishWord,englishWord))
		result = cur.fetchone()
		engId = result[0]
		c.commit()

		inOrSelQuery = "WITH S AS (SELECT id FROM spanish WHERE word = %s), I AS (INSERT INTO spanish (word) SELECT %s WHERE NOT EXISTS (SELECT id FROM spanish WHERE word= %s) RETURNING id) SELECT id FROM I UNION ALL SELECT id from S;"
		cur.execute(inOrSelQuery,(spanishWord,spanishWord,spanishWord))
		result = cur.fetchone()
		espId = result[0]
		c.commit()

		#count = cur.rowcount
		
		print("got engID",engId, "espId",espId)
		#INSERT INTO pairengesp (engId,espId) SELECT 21,11 WHERE NOT EXISTS (SELECT id FROM pairengesp WHERE engId = 21 AND espId = 11);
		insertQuery = "INSERT INTO pairengesp (engId,espId) SELECT %s, %s WHERE NOT EXISTS (SELECT id FROM pairengesp WHERE engId = %s AND espId = %s)"
		#INSERT INTO pairengesp (engID,espId) SELECT 26 ,53 WHERE NOT EXISTS (SELECT id FROM pairengesp WHERE engId = 26 AND espId = 53)
		cur.execute(insertQuery,(engId,espId,engId,espId))
		count = cur.rowcount
		if count > 0:
			c.commit()
		print("insert pair changed -",count)

	except(Exception,psycopg2.Error) as error:
		print("Error in saveToDb",error)

	finally:
		return count

# WHERE lower(title) SIMILAR TO '(a|k|t)%'
#INSERT INTO english (word) SELECT 'arrives' WHERE NOT EXISTS (SELECT id FROM english WHERE word = 'arrives';

'''
---Only spanish words starting with ? letter

SELECT pairEngEsp.id,spanish.word,english.word,pairEngEsp.timescorrect,pairEngEsp.timesincorrect FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id WHERE lower(spanish.word) SIMILAR TO 'l%'

---Same as above but order by timescorrect
SELECT pairEngEsp.id,spanish.word,english.word,pairEngEsp.timescorrect,pairEngEsp.timesincorrect FROM english INNER JOIN pairEngEsp ON english.id = pairEngEsp.engId INNER JOIN spanish ON pairEngEsp.espId = spanish.Id WHERE lower(spanish.word) SIMILAR TO 'l%' ORDER BY timescorrect;


'''