#parent classes
class Animal():
	def __init__(self):
		self.name=''	
class Voice():
	def __init__(self):
		self.voice=''
# first level herit parent Animal
class One(Animal):
	def __init__(self,name):
		super().__init__()
		self.name=name						
	def talk(self):
		print(f'I am a {self.name} !')	
# second level herit parent One
class Twice(One):
	def __init__(self,name,voice):
		super().__init__(name)
		self.voice=voice						
	def talk(self):
		print(f'I am a {self.name} ! And I {self.voice}')	
#multiple herit Animal,Voice
class Multiple(Animal, Voice):	
	def __init__(self,name,voice):
		super().__init__()
		self.name=name
		self.voice=voice						
	def talk(self):
		print(f'I am a {self.name} and I say {self.voice}')


	
		
			
				
					
						
							
								
										
	
			
cat=One('cat')
cat.talk()
cat=Twice('cat','meow')
cat.talk()
cat=Multiple('cat','miaou')
cat.talk()


dog=Multiple('dog','waouf')
dog.talk()
	