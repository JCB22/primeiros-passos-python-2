# Seq 1 to 9,000,000
# obter cada numero da sequencia ao cubo

import sys

def mygenerator(n):
    for x in range(n):
        yield x ** 3

values = mygenerator(100)

print(sys.getsizeof(values))
