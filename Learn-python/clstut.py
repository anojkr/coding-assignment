class Employee:

	def __init__(self, first_name, last_name, salary, increment):
		self.first_name  = first_name 
		self.last_name   =  last_name
		self.name = first_name + ' '+ last_name
		self.salary = salary + (salary*increment)/100

	@property
	def email(self):
		return self.first_name + '.' +self.last_name + '@gmail.com'

	@email.setter
	def email(self, name):
		f_name, l_name = name.split(' ')
		self.first_name = f_name
		self.last_name = l_name
		self.name = f_name + ' ' +l_name
		return 


emp = Employee('anoj', 'kumar', 10000, 5)

print(emp.name)
print(emp.email)
print(emp.salary)

emp.email = 'vinod keshav'
print(emp.name)
print(emp.email)
print(emp.salary)
