import sys
from operator import attrgetter

class Dog:
	species = 'mammal'

	#Constructor de la clase Dog
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	#Método que comprueba si el animal es un mamífero. Ahora mismo, siempre
	#lo es porque no hay herencia.
	def check(self):
		if self.species == 'mammal':
			print('{} is a {}'.format(self.name,self.species))	

	#Método que devuelve un literal con el nombre y la edad del animal
	def dump(self):
		return '{} is {}'.format(self.name,self.age)

	#Método que devuelve un literal comparando la edad de dos animales
	def compare(self,other):
#		print ('{} is {} and {} is {}'.format(self.name,self.age,other.name,other.age))
		print ('{} and {}'.format(self.dump(),other.dump()))

	def get_biggest_number(self,*nums):
#		print('I have been provided with {} numbers. The highest one is {}'.format(nums,max(nums)))
		return max(*nums)

	#Compara la edad de varios animales y devuelve un literal con el nombre del que tiene mayor edad
	def get_oldest(self,*dogs):
		#Utiliza la función attrgetter() para encontrar la edad de cada uno de los animales
		#Convertimos un tuple (inmutable) a una lista usando la función list()
		m = max(self,*list(dogs),key=attrgetter('age'))
		print('I am comparing {} with {} other dog(s). The oldest one is {}.'.format(self.name,len(dogs),m.name))

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


	bambi.get_oldest(micky,simba,pumbaa)
	simba.get_oldest(micky,bambi,pumbaa)

if __name__ == '__main__':
	sys.exit(main())

