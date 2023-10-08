'''
Polar coordinates are an alternative way of representing Cartesian 
coordinates or Complex Numbers.

You are given a complex `z`. Your task is to convert it to polar 
coordinates.
'''

from cmath import sqrt, atan, pi, phase

if __name__ == '__main__':
    z = complex(input())
    x, y = z.real, z.imag

    print(sqrt(x**2 + y**2).real)
    print(phase(z))