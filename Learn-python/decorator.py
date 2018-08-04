import time
import random
def decorator_maker(*argd, **ard):
	print("I am decorator maker with argument {} , {}".format(argd,ard))
	def decorator(func):
		def wrapper(*argf, **arf):
			before = time.time()
			r = func(*argf, **arf)
			print("I am decorator maker with argument {}, {}, {}, {}".format(argd,ard, argf, arf))
			after = time.time()
			print("Time Delay {}".format(after-before))
			return func
		print("Closing wrapper")
		return wrapper
	print("Closing argument maker")
	return decorator

@decorator_maker("test", name='Anoj')
def add(a ,b):
	print("Sum {}".format(a+b))
	return a+b


add(5,7)