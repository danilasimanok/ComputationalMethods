# Computational Methods

## Task 1

- source file: conds.py
- tests:
	- m1, 1, -1
	- m2, 1, 1
	- m3, 1, -1
	- m4, 0, 0
	- hilbert, 3, -1
- conclusions:
	- m1, m3, hilbert => grand conds lead to grand errors
	- m2 => method inaplicable for identity matrix
	- m4 => method inaplicable for some tridiagonal matrix

## Task 2

- source files:
	- lu_decomposition.py
	- regularisation.py
- conclusions:
	- conds change during LU decomposition
	- best alphas in regularisation do not match

## Task 3

- source file: qr_decomposition.py
- conclusion: sometimes cond_s grow up, but other conds always go down

## Task 5

- source file: eigenvalue.py
- conclusions:
	- the less is the epsilon the more iterations are needed
	- scal_method is better

## Task 6

- source file: jacobi.py
- conclusions:
	- The more is precision, the more iterations are needed.
	- Found eigenvalues are in Gershgorin circles.

## Task 7

- source file: grid_method.py
- conclusions are obvious

## Task 8

- source file: galerkin.py
- conclusion: the bigger is N the better is solution

## Task 10

- source file: thermal_conductivity.py
- conclusion: if stability condition isn't met, the figure is not indicative
