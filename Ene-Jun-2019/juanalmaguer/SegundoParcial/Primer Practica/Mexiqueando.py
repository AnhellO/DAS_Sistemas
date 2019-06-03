countries = {
	'agu': 'aguascalientes',
	'bcn': 'baja california',
	'bcs': 'baja california',
	'cam': 'campeche',
	'chp': 'chiapas',
	'chh': 'chihuahua',
	'cmx': 'ciudad de méxico',
	'coa': 'coahuila',
	'col': 'colima',
	'dur': 'durango',
	'gua': 'guanajuato',
	'gro': 'guerrero',
	'hid': 'hidalgo',
	'jal': 'jalisco',
	'mex': 'méxico',
	'mic': 'michoacán',
	'mor': 'morelos',
	'nay': 'nayarit',
	'nle': 'nuevo león',
	'oax': 'oaxaca',
	'pue': 'puebla',
	'que': 'querétaro',
	'roo': 'quintana roo',
	'slp': 'san luis potosí',
	'sin': 'sinaloa',
	'son': 'sonora',
	'tab': 'tabasco',
	'tam': 'tamaulipas',
	'tla': 'tlaxcala',
	'ver': 'veracruz',
	'yuc': 'yucatán',
	'zac': 'zacatecas'
}

#for item in countries.keys():
for key, values in countries.items():
   print (key, "es el código ISO 3166-2 para el estado de",values)
list(sorted(countries.keys()))
