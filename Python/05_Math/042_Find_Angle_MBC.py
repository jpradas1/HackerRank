'''
`ABC` is a right triangle, at `B`.
Therefore, the angle `ABC` = 90°.

Point `M` is the midpoint of hypotenuse `AC`.

You are given the lengths `AB` and `BC`.
Your task is to find the angle formed in `MBC` (angle `theta`, as shown in 
the figure) in degrees.
'''

from cmath import atan, pi

if __name__ == '__main__':
    AB = float(input())
    BC = float(input())

    theta = atan(AB/BC).real * 180 / pi
    decimal_part = theta % 1

    if decimal_part >= 0.5:
        theta = int(theta + 1)
    else:
        theta = int(theta)

    print(f'{theta}'+ u'\N{DEGREE SIGN}')