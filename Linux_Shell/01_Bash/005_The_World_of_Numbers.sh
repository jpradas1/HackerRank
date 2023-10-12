#!/bin/bash

# Two lines containing one integer each (`X` and `Y`, respectively).
# Four lines containing the sum `(X+Y)`, difference `(X-Y)`, product `(X*Y)`,
# and quotient `(X/Y)`, respectively.
# (While computing the quotient, print only the integer part.)

read X
read Y

echo "$(($X+$Y))"
echo "$(($X-$Y))"
echo "$(($X*$Y))"
echo "$(($X/$Y))"