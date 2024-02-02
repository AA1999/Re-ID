from math import sqrt


def is_prime(number):
	if not isinstance(number, int):
		return False
	if number < 2:
		return False
	return all(number % div != 0 for div in range(2, int(sqrt(number)) + 1))


primes = [prime for prime in range(0, 200000) if is_prime(prime)]
primes_string = ''.join(str(prime) for prime in primes)


def solution(i):
	print(primes_string[i: i + 5])
	
solution(100)
