import psycopg2
from NonEngConversion import*

def getConnection():
	conn = psycopg2.connect(database = "engEspDeuDb", user = "justin", password = "password", host = "127.0.0.1", port = "5432")
	print(conn.encoding)
	#conn.set_client_encoding('UNICODE')
	#print(conn.encoding)
	return conn

needsDecoding = False
c = getConnection()
cur = c.cursor()
cur.execute("SHOW SERVER_ENCODING")
rows = cur.fetchall()
for row in rows:
	encoding = row[0]
	if (encoding == "UTF8"):
		print("Database is using UTF8 encoding")
		
		needsDecoding = True

if needsDecoding:
	cur.execute("SELECT spanish.word FROM spanish")
	rows = cur.fetchall()
	i = 0
	

	for row in rows:
		word = row[0]
		bNonEng = ContainsNonEngChars(word)
		print(word,bNonEng)
		if (bNonEng):
			word = replaceWithLatin1Char(word)
			print(word)


'''
			people = [u'Addem\xe1s', u'Andr\xe9']

			print(people[0])
			print(people[1]) """

		i += 1
		#decode = word.decode('utf8')
		#a = 'Entre\xc3\xa9'
		#b = a.decode('utf8')
		#print(b)
		#print("\tSpanish Word = ", row[1], end = '')
		#print("\tEnglish Word = ", row[2])
		'''
		
c.close()