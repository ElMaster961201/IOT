import firebase_admin
import time

from firebase_admin import credentials
from firebase_admin import db

from Motor import Motor

# Instanciamos la clase motor. 
motor = Motor()

# Fetch the service account key JSON file contents
cred = credentials.Certificate('iotp-b39ea-firebase-adminsdk-m9fih-72626cd483.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iotp-b39ea.firebaseio.com'
})

# Muestra la informacion en la base de datos. 
def muestra(a):
    for k, v in a.items():
        
        # print(type(v))
        if isinstance(v, dict):
            muestra(v)
        elif isinstance(v, list):
            r = v[1]
            for i in v[2:]:
                r = r + ", " + i
                pass
            print()
            print (k + ":", r)
        else:
            print()
            print (k + ":", v)

# Referenciamos a la base de datos y obtenemos los horarios de la comida.
ref1 = db.reference('/paco-chihuahua-pequenno/Horarios')
comida = ref1.get()[1:]

# Referenciamos a la base de datos y obtenemos la cantidad de comida.
ref2 = db.reference('/paco-chihuahua-pequenno/ComidaResipiente')
recipiente = ref2.get()
ref3 = db.reference('/paco-chihuahua-pequenno')

while True:
    for H in comida:
        # Se recupera la hora.
        localtime = time.localtime(time.time())
        h = H.split(":") 
        if int(h[0]) == localtime[3] and int(h[1]) == localtime[4]:

            # Activamos el motor para que suelte comida.
            motor.steps(120)
            time.sleep(3)
            motor.steps(-120)

            # Actualiza la base de datos 
            ref3.update( {"ComidaResipiente":str (int(recipiente) - 5)})
            
            # Actualizo mi variable de comida en el resipiente.
            recipiente = ref2.get()
            
            # El programa tiene un tiempo de espera de 5 minutos antes de continuar.
            time.sleep(300)
            
            pass
        pass
    pass