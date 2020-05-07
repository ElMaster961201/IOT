from firebase import firebase
firebase = firebase.FirebaseApplication('https://iotp-b39ea.firebaseio.com', None)

data = {
	'Name':'Jesus',
	'Email':'@gmail.com' 
}

# Envio de informacion.
#result = firebase.post('/user',data)

# print (result)
#Descarga de informacion.
result = firebase.get('/user',None)

re = result.values()

for r in re:
	sr = r.items()
	for k,v in sr:
		print (k,"   ",v)
		pass
	print()

#print(result['-M6kB5sxDF8FUQSvfNv3'])
#print (result[list(result.keys())])
