#!/usr/bin/env python 
#-*-coding: latin-1-*-
# libraries
import time
import RPi.GPIO as GPIO

class Motor(object):
	def __init__(self):
		# Use BCM GPIO references
		# Instead of physical pin numbers
		GPIO.setmode(GPIO.BCM)
		# Define GPIO signals to use Pins 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
		self.StepPins = [24,25,8,7]

		self.nbStepsPerRev=760 #Pasos necesarios para dar una vuelta

		# Set all pins as output
		for pin in self.StepPins:
			#print ("Setup pins")
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, 0) #False)
			pass
		# Define some settings
		self.WaitTime = 0.001
		# Define simple sequence
		self.Seq1 = [
						[1,0,0,0],
						[0,1,0,0],
						[0,0,1,0],
						[0,0,0,1]
					]
		# Define advanced half-step sequence
		self.Seq2 = [
						[1,0,0,0],
						[1,1,0,0],
						[0,1,0,0],
						[0,1,1,0],
						[0,0,1,0],
						[0,0,1,1],
						[0,0,0,1],
						[1,0,0,1]
					]
		self.StepCount = len(self.Seq2)
		self.Seq = self.Seq2
		pass

	def steps(self):
		nb = self.nbStepsPerRev
		StepCounter = 0
		if nb<0: 
			sign=-1
		else: 
			sign=1

		nb=sign*nb*2 #times 2 because half-step
		for _ in range(nb):
			for pin in range(4):
				xpin = self.StepPins[pin]
				if self.Seq[StepCounter][pin]!=0:
					GPIO.output(xpin, True)
					time.sleep(self.WaitTime)
				else:
					GPIO.output(xpin, False)
					StepCounter += sign
					time.sleep(self.WaitTime)
					# If we reach the end of the sequence
					pass
				# start again
				if (StepCounter==self.StepCount):
					StepCounter = 0
					pass
				if (StepCounter<0):
					StepCounter = self.StepCount-1
					pass
				pass
			# Wait before moving on
			time.sleep(self.WaitTime)
			pass
		pass

	pass


# Si se ejecuta el archivo.
if __name__ == "__main__":

	# Desavilitamos los warnings
	# GPIO.setwarnings(False)
	# Use BCM GPIO references
	# Instead of physical pin numbers
	GPIO.setmode(GPIO.BCM)
	# Define GPIO signals to use Pins 18,22,24,26 GPIO24,GPIO25,GPIO8,GPIO7
	StepPins = [24,25,8,7]

	try:
		# Set all pins as output
		for pin in StepPins:
			#print ("Setup pins")
			GPIO.setup(pin,GPIO.OUT)
			GPIO.output(pin, 0) #False)
			pass
		# Define some settings
		WaitTime = 0.001
		# Define simple sequence
		StepCount1 = 4
		Seq1 = [
				[1,0,0,0],
				[0,1,0,0],
				[0,0,1,0],
				[0,0,0,1]
			]
		# Define advanced half-step sequence
		StepCount2 = 8
		Seq2 = [
				[1,0,0,0],
				[1,1,0,0],
				[0,1,0,0],
				[0,1,1,0],
				[0,0,1,0],
				[0,0,1,1],
				[0,0,0,1],
				[1,0,0,1]
			]

		# Choose a sequence to use
		Seq = Seq2
		StepCount = StepCount2

		def steps(nb):
			StepCounter = 0
			if nb<0: 
				sign=-1
			else: 
				sign=1

			nb=sign*nb*2 #times 2 because half-step
			print("nbsteps {} and sign {}".format(nb,sign))
			for _ in range(nb):
				for pin in range(4):
					xpin = StepPins[pin]
					if Seq[StepCounter][pin]!=0:
						GPIO.output(xpin, True)
						time.sleep(WaitTime)
					else:
						GPIO.output(xpin, False)
						StepCounter += sign
						time.sleep(WaitTime)
						# If we reach the end of the sequence
						pass
					# start again
					if (StepCounter==StepCount):
						StepCounter = 0
						pass
					if (StepCounter<0):
						StepCounter = StepCount-1
						pass
					pass
				# Wait before moving on
				time.sleep(WaitTime)
				pass
			pass

		# Start main loop
		nbStepsPerRev=760 #Pasos necesarios para dar una vuelta
		hasRun=False
		while not hasRun:
			steps(nbStepsPerRev)# parcourt un tour dans le sens horaire
			time.sleep(1)
			steps(-nbStepsPerRev)# parcourt un tour dans le sens anti-horaire
			time.sleep(1)
			hasRun=True
			print ("Stop motor")
			for pin in StepPins:
				GPIO.output(pin, False)
				pass
			pass
	finally:
		# Reiniciar todos los canales de GPIO.
		GPIO.cleanup()