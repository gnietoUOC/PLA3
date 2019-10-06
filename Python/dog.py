import sys
from operator import attrgetter

class Dog:
	species = 'mammal'

	def __init__(self,name,age):
		""" Constructor de la clase Dog 
		"""
		self.name = name
		self.age = age
	

	def check(self):
		""" Método que comprueba si el animal es un mamífero. Ahora mismo, siempre
			lo es porque no hay herencia.
		"""
		if self.species == 'mammal':
			print('{} is a {}'.format(self.name,self.species))	


	def dump(self):
		""" Método que devuelve un literal con el nombre y la edad del animal
		"""
		return '{} is {}'.format(self.name,self.age)

		""" Método que devuelve un literal comparando la edad de dos animales
		"""
	def compare(self,other):
		""" Compara dos elementos de la clase Dog 
		"""
		print ('{} and {}'.format(self.dump(),other.dump()))

	def get_biggest_number(self,*nums):
		return max(*nums)

	def get_oldest(self,*dogs):
		""" Compara la edad de varios animales y devuelve un literal con el nombre del que tiene mayor edad
			* Utiliza la función attrgetter() para encontrar la edad de cada uno de los animales
			* Convertimos un tuple (inmutable) a una lista usando la función list()
		"""
		return max(self,*list(*dogs),key=attrgetter('age'))

def main():

	bambi = Dog('bambi',5)
	micky = Dog('micky',6)

	print(bambi.dump())
	print(micky.dump())

	simba = Dog('simba',10)
	pumbaa = Dog('pumbaa',4)
	timon = Dog('timon',8)

	print(simba.dump())
	print(pumbaa.dump())
	print(timon.dump())

	bambi.compare(micky)
	bambi.check()

	nums = [1,3,5,7,4,2]
	m = bambi.get_biggest_number(nums)
	print('I have been provided with {} numbers ({}). The highest one is {}.'.format(len(nums),nums,m))

	dogs = [micky,simba,pumbaa];
	m2 = bambi.get_oldest(dogs)
	print('I am comparing {} with {} other dog(s). The oldest one is {}.'.format(bambi.name,len(dogs),m2.name))

if __name__ == '__main__':
	sys.exit(main())

