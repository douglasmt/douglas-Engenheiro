# Let's define a speed_test decorator
from functools import wraps
from time import time

def speed_test(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		start_time = time()
		
		result = fn(*args, **kwargs) 
		# calls the function with decoration() 
		# sum_nums_gen or sum_nums_list

		end_time = time()
		print(f"\nExecuting: {fn.__name__}")
		print(f"Time Elapsed: {end_time - start_time} \n")
		return result
	return wrapper

@speed_test
def sum_nums_gen():
	return f'Total sum: {sum(x for x in range(90000000))} \n'

@speed_test
def sum_nums_list():
	return f'Total sum: {sum([x for x in range(90000000)])}\n '


print(sum_nums_gen()) # 	GEN ()  	- always call the decorator @speed_test
print(sum_nums_list()) # 	LIST ([]) 	- always call the decorator @speed_test


