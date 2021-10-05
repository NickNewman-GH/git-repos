# this is test project for git testing
from functools import lru_cache

@lru_cache(1024)
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n - 1) + fib(n - 2)

print(fib(64))