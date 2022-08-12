import keyboard
datadict={'ADD': 'Your Full Address With Pincode',
 'CITY': 'Your City Name',
 'EMAIL': 'youremailaddress@gmail.com',
 'SCH': 'Your School Name With Full Address'}
mylist=list(datadict.keys())
for short in mylist:
	print('%10s : %s' %(short,datadict[short]))
keyboard.add_abbreviation('SCH', datadict['SCH'])
keyboard.add_abbreviation('CITY', datadict['CITY'])
keyboard.add_abbreviation('EMAIL', datadict['EMAIL'])
keyboard.add_abbreviation('ADD', datadict['ADD'])
