class Parole():
	interjection=''
	sujet=''
	verbe=''
	attribut=''
	animal=''
	
	def __init__(self,animal):
		self.animal=animal
		
	def __repr__(self):
		return self.interjection+self.sujet+self.verbe+self.attribut+self.animal
		
class Canard(Parole):
	def __init__(self):
		self.interjection='Brrrr ! '
		self.sujet='Il '
		self.verbe='fait '
		self.attribut='un froid de '
		self.animal='canard'	
		
canard=Canard()
print(canard)


class Poule(Parole):
	def __init__(self):
		self.interjection='Je sais ! '
		self.sujet='J\'en '
		self.verbe='ai '
		self.attribut='la chair de '
		self.animal='poule'
			
poule=Poule()
print(poule)

class Caille(Parole):
	def __init__(self):
		self.interjection='Oui ! '
		self.sujet='Ca '
		self.animal='caille'
		
caille=Caille()
print(caille)