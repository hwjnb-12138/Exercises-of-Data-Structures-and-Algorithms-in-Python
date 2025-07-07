# Describe a recursive function for computing the nth Harmonic number

def harmonic_number(n):
    if n == 1:
        return 1

    return 1/n + harmonic_number(n-1)
