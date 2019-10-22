import sys
from operator import attrgetter


class Dog(object):
	species = 'mammal'

	def __init__(self, name, age):
		""" Constructor de la clase Dog.
		"""
		self.name = name
		self.age = age
	

	def check(self):
		""" Método que comprueba si el animal es un mamífero. Ahora mismo, 
			siempre lo es porque no hay herencia.
		"""
		if self.species == 'mammal':
			print('{name} is a {species}'.format(
				name = self.name,
				species = self.species))	


	def dump(self):
		""" Método que devuelve un literal con el nombre y la edad del animal.
		"""
		return '{name} is {age}'.format(
			name = self.name,
			age = self.age)

	def compare(self, other):
		""" Método que devuelve un literal comparando la edad de dos animales. 
		"""
		print ('{dump1} and {dump2}'.format(
			dump1 = self.dump(),
			dump2 = other.dump()))

	@staticmethod
	def get_biggest_number(*nums):
		""" Devuelve el máximo de los valores de una lista. Lo he creado 
			como método estático ya que realmente no tiene nada que ver con 
			la clase.
			Gracias a las 'bondades' de Python, este método también funciona 
			con otros tipos de datos que no sean enteros, por ejemplo con cadenas. 
			No he añadido la validación de que los elementos sean enteros. 
		""" 
		return max(*nums)

	@staticmethod
	def get_oldest(*dogs):
		""" Compara la edad de varios animales y devuelve un literal con el 
			nombre del que tiene mayor edad.
			* He definido el método como estático porque me ha parecido más 
			  coherente.
			* Utiliza la función attrgetter() para encontrar la edad de cada 
			  uno de los animales
			* Convertimos un tuple (inmutable) a una lista usando la función 
			  list()
		"""
		return max(*list(*dogs),key=attrgetter('age'))


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

	m = Dog.get_biggest_number(3,2,1,4,9,5,0)
	print('The highest value is {max}.'.format(max = m))
	nums = [1,3,5,7,4,2]
	m = Dog.get_biggest_number(nums)
	print('I have been provided with {n} numbers ({nums}). The highest one is {max}.'.format(
		n = len(nums),
		nums = nums,
		max = m))

	dogs = [bambi,micky,simba,pumbaa,timon];
	m2 = Dog.get_oldest(dogs)
	print('I am comparing {name1} with {n} other dog(s). The oldest one is {name2}.'.format(
		name1 = bambi.name,
		n = len(dogs),
		name2 = m2.name))

if __name__ == '__main__':
	sys.exit(main())

