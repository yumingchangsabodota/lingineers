

class Vowel_Lists():

	vowel_lists = {
					'english':
					[{'vowel':'a','action':'Next', 'next':'e'},
					{'vowel':'e','action':'Next', 'next':'i'},
					{'vowel':'i','action':'Next', 'next':'o'},
					{'vowel':'o','action':'Next', 'next':'u'},
					{'vowel':'u','action':'Process', 'next':'to-formants'}]
					}


	dummy_formants = {'data':[
		{'y':342,'x':2322},
		{'y':427,'x':2365},
		{'y':476,'x':2530},
		{'y':580,'x':2058},
		{'y':588,'x':2349},
		{'y':768,'x':1551},
		{'y':652,'x':1136},
		{'y':497,'x':1035},
		{'y':469,'x':1225},
		{'y':378,'x':1105},
		{'y':623,'x':1426},
		{'y':474,'x':1379},
	], 'labels':['i','ɪ','e','ɛ','æ','ɑ','ɔ','o','ʊ','u','ʌ','ɜ']}