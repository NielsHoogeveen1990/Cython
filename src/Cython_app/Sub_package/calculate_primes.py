# import pyximport
# pyximport.install()

from Cython_app.Cython_package.primes import get_primes

def calculate_primes(nb_primes):
    print(get_primes(nb_primes))


# if __name__=='__main__':
#     calculate_primes(100)