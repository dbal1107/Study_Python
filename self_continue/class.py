class Human() : 
	'''인간'''
	def __init__(self, name, weight) : 
		'''초기화 함수 : 초기화하여 인스턴스(person) 불러옴'''
		print('__init__실행')
		self.name = name
		self.weight = weight
		print('이름은 {}, 몸무게는 {}'.format(self.name, self.weight))

	def __str__(self) : 
		'''문자열화 함수 : 문자열로 어떻게 보여줄지'''
		print('__str__실행')
		return '이름은 {}, 몸무게는 {}'.format(self.name, self.weight)

	def eat(self) : 
		self.weight += 0.1
		print('{}가 먹어서 {}kg이 되었습니다.'.format(self.name, self.weight))
	
	def walk(self) : 
		self.weight -= 0.1
		print('{}가 걸어서 {}kg이 되었습니다.'.format(self.name, self.weight))

	def speak(self, message) : 
		print(message)

# person = Human() # -> __init__실행 출력
person = Human('사람', 60)
print(person)