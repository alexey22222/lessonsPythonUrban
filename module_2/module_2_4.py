numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primers = []
is_prime = True
def _prime_(elements):
    for i in range(2,  elements ):
        if (elements%i) == 0:
            return False
    return True
for i in range(len(numbers)):
    is_prime = _prime_(numbers[i])
    if numbers[i] == 1:
        continue
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primers.append(numbers[i])
print('Primers:', primes)
print('Not Primers:', not_primers)
