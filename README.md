# English Spanish Pair
An application to match the meaning of english and spanish words, written in python and using a postgres database.

#### EspEngPair1.0
This is the main part which uses a tkinter canvas for words to move across the window.
Words are selected using the mouse pointer. If the correct two words are selected both will move up the screen until they are no longer visible.
If the selected pair is incorrect both will flash red and be automatically unselected.
When all words are successfully moved off screen a new set of pairs will move in to view.
Simple collision detection is used to prevent words from being placed on top of one another.

![screenshot](/screenshots/EspEngPairSS1.png)

#### pairDb
This is the code for interaction with the database.
Can read all pairs from db, update values of number of times a particular pair was correct or incorrect.
Also contains code for creating new pairs by adding both english and spanish words and linking them in the pair table.

#### readFileLines
A runnable file that will read pairs from a text file.
Any word or pair that already exists in the database will not be added again.

![screenshot](/screenshots/readFileLinesSS1.png)

#### esp_SomeWords.txt
The text file which can be read by 'readFileLines.py' to add words and pairs to database.
Each line starts with a spanish word then a space followed by a colon to inform end of spanish word.
All spaces will then be ignored until a non-space character to inform start of english word space after english word terminates end of line.
Lines starting with '//' will be ignored.

This is to make it simple to add new data to the database without creating duplicates.
Program will be needed in future for more convenient method of data input and editing.
