class Student:
	school_name = 'XYZ'

	def __init__(self, name, clas, age):
		self.name = name
		self.clas = clas
		self.age = age

	# @classmethod
	# def school(cls, school_name):
	# 	cls.school_name = school_name

	def details(self):
		print("{}, {}, {}".format(self.name, self.clas, self.age))

	@classmethod
	def set_details(cls, dem):
		name , clas, age = dem.split(' ')
		return cls(name, clas, age)




s = Student('anoj', 'V', 15)
s.details()
x = Student.set_details('vinod VII 17')
x.details()