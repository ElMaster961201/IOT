from firebase import firebase
firebase = firebase.FirebaseApplication('https://iotp-b39ea.firebaseio.com', None)

data = {
	'Name':'Jesus',
	'Email':'@gmail.com' 
}

# Envio de informacion.
# Crea  una referencia tipo objeto.
#result = firebase.post('/user',data)

# Envia informacion.
# Tal y cual como aparece despues de la ruta.
firebase.put('/user','2',data)

# Elimina el objeto
# firebase.delete('/user','-M6kB5sxDF8FUQSvfNv3')

# print (result)
#Descarga de informacion.
result = firebase.get('/user', None)[1:]

for r in result:
	print ()
	print(r)
	for v,k in r.items():
		print (v, "    ", k)
		pass
	pass

#print(result['-M6kB5sxDF8FUQSvfNv3'])
#print (result[list(result.keys())])
