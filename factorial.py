from functools import lru_cache

@lru_cache(32)
def fac(n):
	if n == 1:
		return n
	return n*fac(n-1)

print(fac(6))